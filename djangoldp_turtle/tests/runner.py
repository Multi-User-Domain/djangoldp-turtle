import sys
import yaml

import django
from django.conf import settings as django_settings
from djangoldp.conf.ldpsettings import LDPSettings
from djangoldp.tests.settings_default import yaml_config

# override config loading
config = {
    # add the packages to the reference list
    'ldppackages': ['djangoldp.tests', 'djangoldp_turtle', 'djangoldp_turtle.tests'],

    # required values for server
    'server': {
        'AUTH_USER_MODEL': 'tests.User',
        'REST_FRAMEWORK': {
            'DEFAULT_PAGINATION_CLASS': 'djangoldp.pagination.LDPPagination',
            'PAGE_SIZE': 5
        },
        # map the config of the core settings (avoid asserts to fail)
        'SITE_URL': 'http://happy-dev.fr',
        'BASE_URL': 'http://happy-dev.fr',
        'SEND_BACKLINKS': False,
        'JABBER_DEFAULT_HOST': None,
        'ANONYMOUS_USER_NAME': None,
        'SERIALIZER_CACHE': False
    }
}
ldpsettings = LDPSettings(config)
ldpsettings.config = yaml.safe_load(yaml_config)

django_settings.configure(ldpsettings)

django.setup()
from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner(verbosity=1)

failures = test_runner.run_tests([
    'djangoldp_turtle.tests.tests_view',
])
if failures:
    sys.exit(failures)
