import pytest
from dev.fixture.application import Application

fixture = None

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.login_to_system(name="Lead Tiller", password="Gmtfree123")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(end)

