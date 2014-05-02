package com.uia.example.my;

import com.android.uiautomator.core.UiDevice;
import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class LaunchGooglePlayOnNexus5 extends UiAutomatorTestCase {

	public void testDemo() throws UiObjectNotFoundException {

		UiDevice device = getUiDevice();
		device.pressHome();

		String currentPackageName = device.getCurrentPackageName();
		assertEquals("com.android.launcher3", currentPackageName);

		UiObject apps = new UiObject(new UiSelector().text("Apps"));
		apps.click();

		UiObject pageIndicator = new UiObject(new UiSelector().resourceId("com.android.launcher3:id/page_indicator"));
		int pageCount = pageIndicator.getChildCount();

		for (int i = 0; i < pageCount; i++) {
			UiObject app = new UiObject(new UiSelector().text("Play Store"));
			boolean isAppExist = app.waitForExists(0);
			if(isAppExist){
				app.click();
				break;
			}
			else{
				UiObject page = new UiObject(new UiSelector().resourceId("com.android.launcher3:id/apps_customize_pane_content"));
				page.swipeLeft(10);
			}
		}
	}
}