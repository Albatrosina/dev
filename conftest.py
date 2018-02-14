import pytest
from dev.fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login_to_system(name="Lead Tiller", password="Gmtfree123")
    request.addfinalizer(fixture.destroy())
    return fixture

