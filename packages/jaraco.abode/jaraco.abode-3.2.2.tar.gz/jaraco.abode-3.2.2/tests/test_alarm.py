"""Test the Abode device classes."""
import jaraco.abode
from jaraco.abode.helpers import urls
import jaraco.abode.helpers.constants as CONST
import pytest

from .mock import login as LOGIN
from .mock import oauth_claims as OAUTH_CLAIMS
from .mock import logout as LOGOUT
from .mock import panel as PANEL
from .mock import devices as DEVICES
from .mock.devices import alarm as ALARM


class TestAlarm:
    """Test the Alarm class."""

    def test_abode_alarm_setup(self, m):
        """Check that Abode alarm device is set up properly."""
        panel = PANEL.get_response_ok(mode=CONST.MODE_STANDBY)
        alarm = ALARM.device(area='1', panel=panel)

        m.post(urls.LOGIN, json=LOGIN.post_response_ok())
        m.get(urls.OAUTH_TOKEN, json=OAUTH_CLAIMS.get_response_ok())
        m.get(urls.DEVICES, json=DEVICES.EMPTY_DEVICE_RESPONSE)
        m.get(urls.PANEL, json=PANEL.get_response_ok())

        alarm_device = self.client.get_alarm()

        assert alarm_device is not None

        assert alarm_device._state == alarm

    def test_alarm_device_properties(self, m):
        """Check that the abode device properties are working."""
        # Set up URLs
        m.post(urls.LOGIN, json=LOGIN.post_response_ok())
        m.get(urls.OAUTH_TOKEN, json=OAUTH_CLAIMS.get_response_ok())
        m.post(urls.LOGOUT, json=LOGOUT.post_response_ok())
        m.get(
            urls.PANEL,
            json=PANEL.get_response_ok(
                mode=CONST.MODE_STANDBY,
                battery=True,
                is_cellular=True,
                mac='01:AA:b3:C4:d5:66',
            ),
        )
        m.get(urls.DEVICES, json=DEVICES.EMPTY_DEVICE_RESPONSE)

        # Logout to reset everything
        self.client.logout()

        # Get alarm and test
        alarm = self.client.get_alarm()
        assert alarm.device_id == 'area_1'
        assert alarm is not None
        assert alarm.mode == CONST.MODE_STANDBY
        assert alarm.status == CONST.MODE_STANDBY
        assert alarm.battery
        assert alarm.is_cellular
        assert not alarm.is_on
        assert alarm.device_uuid == '01aab3c4d566'
        assert alarm.mac_address == '01:AA:b3:C4:d5:66'

        # Change alarm properties and state to away and test
        m.get(
            urls.PANEL,
            json=PANEL.get_response_ok(
                mode=CONST.MODE_AWAY, battery=False, is_cellular=False
            ),
        )

        # Refresh alarm and test
        alarm.refresh()

        assert alarm.device_id == 'area_1'
        assert alarm.mode == CONST.MODE_AWAY
        assert alarm.status == CONST.MODE_AWAY
        assert not alarm.battery
        assert not alarm.is_cellular
        assert alarm.is_on

        # Change alarm state to final on state and test
        m.get(urls.PANEL, json=PANEL.get_response_ok(mode=CONST.MODE_HOME))

        # Refresh alarm and test
        alarm.refresh()
        assert alarm.mode == CONST.MODE_HOME
        assert alarm.status == CONST.MODE_HOME
        assert alarm.is_on

    def test_alarm_device_mode_changes(self, m):
        """Test that the abode alarm can change/report modes."""
        # Set up URLs
        m.post(urls.LOGIN, json=LOGIN.post_response_ok())
        m.get(urls.OAUTH_TOKEN, json=OAUTH_CLAIMS.get_response_ok())
        m.post(urls.LOGOUT, json=LOGOUT.post_response_ok())
        m.get(urls.PANEL, json=PANEL.get_response_ok(mode=CONST.MODE_STANDBY))
        m.get(urls.DEVICES, json=DEVICES.EMPTY_DEVICE_RESPONSE)

        # Logout to reset everything
        self.client.logout()

        # Assert that after login we have our alarm device with standby mode
        alarm = self.client.get_alarm()

        assert alarm is not None
        assert alarm.status == CONST.MODE_STANDBY

        # Set mode URLs
        m.put(
            urls.panel_mode('1', CONST.MODE_STANDBY),
            json=PANEL.put_response_ok(mode=CONST.MODE_STANDBY),
        )
        m.put(
            urls.panel_mode('1', CONST.MODE_AWAY),
            json=PANEL.put_response_ok(mode=CONST.MODE_AWAY),
        )
        m.put(
            urls.panel_mode('1', CONST.MODE_HOME),
            json=PANEL.put_response_ok(mode=CONST.MODE_HOME),
        )

        # Set and test text based mode changes
        assert alarm.set_mode(CONST.MODE_HOME)
        assert alarm.mode == CONST.MODE_HOME
        assert not alarm.is_standby
        assert alarm.is_home
        assert not alarm.is_away

        assert alarm.set_mode(CONST.MODE_AWAY)
        assert alarm.mode == CONST.MODE_AWAY
        assert not alarm.is_standby
        assert not alarm.is_home
        assert alarm.is_away

        assert alarm.set_mode(CONST.MODE_STANDBY)
        assert alarm.mode == CONST.MODE_STANDBY
        assert alarm.is_standby
        assert not alarm.is_home
        assert not alarm.is_away

        # Set and test direct mode changes
        assert alarm.set_home()
        assert alarm.mode == CONST.MODE_HOME
        assert not alarm.is_standby
        assert alarm.is_home
        assert not alarm.is_away

        assert alarm.set_away()
        assert alarm.mode == CONST.MODE_AWAY
        assert not alarm.is_standby
        assert not alarm.is_home
        assert alarm.is_away

        assert alarm.set_standby()
        assert alarm.mode == CONST.MODE_STANDBY
        assert alarm.is_standby
        assert not alarm.is_home
        assert not alarm.is_away

        # Set and test default mode changes
        assert alarm.switch_off()
        assert alarm.mode == CONST.MODE_STANDBY
        assert alarm.is_standby
        assert not alarm.is_home
        assert not alarm.is_away

        self.client.set_default_mode(CONST.MODE_HOME)
        assert alarm.switch_on()
        assert alarm.mode == CONST.MODE_HOME
        assert not alarm.is_standby
        assert alarm.is_home
        assert not alarm.is_away

        assert alarm.switch_off()
        assert alarm.mode == CONST.MODE_STANDBY
        assert alarm.is_standby
        assert not alarm.is_home
        assert not alarm.is_away

        self.client.set_default_mode(CONST.MODE_AWAY)
        assert alarm.switch_on()
        assert alarm.mode == CONST.MODE_AWAY
        assert not alarm.is_standby
        assert not alarm.is_home
        assert alarm.is_away

        # Test that no mode throws exception
        with pytest.raises(jaraco.abode.Exception):
            alarm.set_mode(mode=None)

        # Test that an invalid mode throws exception
        with pytest.raises(jaraco.abode.Exception):
            alarm.set_mode('chestnuts')

        # Test that an invalid mode change response throws exception
        m.put(
            urls.panel_mode('1', CONST.MODE_HOME),
            json=PANEL.put_response_ok(mode=CONST.MODE_AWAY),
        )

        with pytest.raises(jaraco.abode.Exception):
            alarm.set_mode(CONST.MODE_HOME)

        # Test that an invalid area in mode change response throws exception
        m.put(
            urls.panel_mode('1', CONST.MODE_HOME),
            json=PANEL.put_response_ok(area='2', mode=CONST.MODE_HOME),
        )

        with pytest.raises(jaraco.abode.Exception):
            alarm.set_mode(CONST.MODE_HOME)
