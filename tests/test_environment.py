from pytest import mark

def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

@mark.skip(reason="you can add reasons as to why tests are being skipped")
def test_skip_me_plz():
    assert False


@mark.skip(reason="you can use -rs to see these reasons after you run tests. otherwise they will not be visible during runs (even verbose runs)")
def test_skip_me_plz():
    assert False