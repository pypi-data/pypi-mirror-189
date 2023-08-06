# Repository: https://gitlab.com/quantify-os/quantify-core
# Licensed according to the LICENCE file on the main branch
"""Module containing the pyqtgraph based plotting monitor."""
from enum import Enum
import pprint
from typing import Any, Optional, Tuple
from collections import OrderedDict

from pyqtgraph.Qt import QtCore, QtWidgets

from quantify_core.visualization import _appnope
from quantify_core.visualization.SI_utilities import SI_val_to_msg_str


class QcSnapshotWidget(QtWidgets.QTreeWidget):
    """
    Widget for displaying QcoDes instrument snapshots.
    Heavily inspired by the DataTreeWidget.
    """

    def __init__(self, parent=None, data=None):
        QtWidgets.QTreeWidget.__init__(self, parent)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.setData(data)
        self.setColumnCount(4)
        self.setHeaderLabels(["Name", "Value", "Unit", "Last update"])
        self.nodes = {}
        self.timer_appnope = None

        if _appnope.requires_appnope():
            # Start a timer to ensure the App Nap of macOS does not idle this process.
            # The process is sent to App Nap after a window is minimized or not
            # visible for a few seconds, this ensure we avoid that.
            # If this is not performed very long and cryptic errors will rise
            # (which is fatal for a running measurement)

            self.timer_appnope = QtCore.QTimer(self)
            self.timer_appnope.timeout.connect(_appnope.refresh_nope)
            self.timer_appnope.start(30)  # milliseconds

    def setData(self, data):
        """
        data should be a snapshot dict: See :class: `~quantify_core.data.handling.snapshot`
        """
        self.buildTreeSnapshot(snapshot=data)
        self.resizeColumnToContents(0)

    def buildTreeSnapshot(self, snapshot):
        # exists so that function can be called with no data in construction
        if snapshot is None:
            return

        parent = self.invisibleRootItem()
        for instrument in sorted(snapshot.keys()):
            sub_snap = snapshot[instrument]
            # Name of the node in the self.nodes dictionary
            instrument_name = sub_snap["name"]
            node = self._add_node(parent, instrument_name, instrument_name)
            self._fill_node_recursively(sub_snap, node, instrument_name)

    def _add_node(self, parent, display_string, node_key):
        if node_key not in self.nodes:
            self.nodes[node_key] = QtWidgets.QTreeWidgetItem([display_string, "", ""])
            parent.addChild(self.nodes[node_key])
        node = self.nodes[node_key]
        return node

    def _fill_node_recursively(self, snapshot, node, node_key):
        sub_snaps = {}
        for key in ["submodules", "channels"]:
            sub_snaps.update(snapshot.get(key, {}))

        for sub_snapshot_key in sorted(sub_snaps.keys()):
            sub_snap = sub_snaps[sub_snapshot_key]
            # Some names contain higher nodes, remove them (with underscore) for brevity
            for node_key_part in node_key.split("."):
                sub_snapshot_key = QcSnapshotWidget._remove_left(
                    sub_snapshot_key, node_key_part
                )
            sub_node_key = f"{node_key}.{sub_snapshot_key}"
            sub_node = self._add_node(node, sub_snapshot_key, sub_node_key)
            self._fill_node_recursively(sub_snap, sub_node, sub_node_key)

        # Don't sort keys if we encounter an OrderedDict
        param_snaps = snapshot.get("parameters", {})
        param_snaps_keys = param_snaps.keys()
        if not isinstance(param_snaps, OrderedDict):
            param_snaps_keys = sorted(param_snaps.keys())

        for param_name in param_snaps_keys:
            param_snap = param_snaps[param_name]
            # Depending on the type of data stored in value do different things,
            # currently only blocks non-dicts
            if not "value" in param_snap.keys():
                # Some parameters do not have a value, these are not shown
                # in the instrument monitor.
                continue
            if isinstance(param_snap["value"], dict):
                # Treat dict as submodule and all entries of dict as parameters.
                # If the dict keys are not str, they are converted to str. Use
                # OrderedDict to sort numbers properly.
                pars = OrderedDict()
                for key in sorted(param_snap["value"].keys()):
                    val = param_snap["value"][key]
                    pars[str(key)] = {
                        "value": val,
                        "name": str(key),
                        "ts": param_snap["ts"],
                        "unit": "",
                        "label": "",
                    }
                sub_snap = {"submodules": {param_name: {"parameters": pars}}}
                self._fill_node_recursively(sub_snap, node, node_key)
            else:
                self._add_single_parameter(param_snap, param_name, node, node_key)

    @staticmethod
    def _convert_to_str(value: Any, unit: Optional[str]) -> Tuple[str, str]:
        """If no unit is given, convert to string and apply nice formatting.
        Otherwise make sure to interpret SI unit appropriately.

        Parameters
        ----------
        value:
            Value of parameter
        unit:
            Unit of parameter

        Returns
        -------
        :
            new value and new unit
        """
        if unit is None or unit == "":
            if isinstance(value, Enum):
                # For Enum, don't show class name
                return value.name, ""
            return str(value), ""
        return SI_val_to_msg_str(value, unit)

    def _add_single_parameter(self, param_snap, param_name, node, node_key):
        value_str, unit = self._convert_to_str(param_snap["value"], param_snap["unit"])
        # Omits printing of the date to make it more readable
        if param_snap["ts"] is not None:
            latest_str = param_snap["ts"][11:]
        else:
            latest_str = ""
        param_node_key = f"{node_key}.{param_name}"
        # If node does not yet exist, create a node
        if param_node_key not in self.nodes:
            param_node = QtWidgets.QTreeWidgetItem(
                [param_name, value_str, unit, latest_str]
            )
            node.addChild(param_node)
            self.nodes[param_node_key] = param_node
        else:  # else update existing node
            param_node = self.nodes[param_node_key]
            param_node.setData(1, 0, value_str)
            param_node.setData(2, 0, unit)
            param_node.setData(3, 0, latest_str)

    @staticmethod
    def _remove_left(
        in_string, to_be_removed
    ):  # todo: replace this method with str.removeprefix when at Python 3.9
        # Do not remove if to_be_removed matches the whole in_string
        if in_string != to_be_removed:
            try:
                _, out_string = in_string.split(f"{to_be_removed}_", 1)
                return out_string
            except ValueError:
                pass

        return in_string

    def getNodes(self):
        return pprint.pformat(self.nodes)
