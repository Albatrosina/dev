
def test_r_p_m_fills(app):
    app.action.switch_to_rpm_tab()
    app.action.delete_fills_row()
    app.session.logout_from_system()
