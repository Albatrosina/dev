import pytest
from fixture.application import Application
from model.login import Login

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login_to_system(Login(name="Lead Tiller", password="Gmtfree123"))
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login_to_system(Login(name="Lead Tiller", password="Gmtfree123"))
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.logout_from_system()
        fixture.destroy()
    request.addfinalizer(end)

