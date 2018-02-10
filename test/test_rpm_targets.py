# -*- coding: utf-8 -*-
from dev.model.fill_row import Filling


def test_r_p_m_accept(app):
    app.action.switch_to_rpm_tab()
    app.fill.corn(Filling(bt="20000", fp="5", hta="1", spread="1", roll="1", flex="1", basis="1", note="some test note"))
    app.action.confirm_targets_row()


def test_r_p_m_decline(app):
    app.action.switch_to_rpm_tab()
    app.fill.corn(Filling(bt="20000", fp="5", hta ="1", spread="1", roll="1", flex="1", basis="1", note="some test note"))
    app.action.delete_targets_row()
