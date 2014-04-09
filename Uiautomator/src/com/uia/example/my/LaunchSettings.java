package com.uia.example.my;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiScrollable;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class LaunchSettings extends UiAutomatorTestCase {

	public void testDemo() throws UiObjectNotFoundException {

		getUiDevice().pressHome();

		UiObject allAppsButton = new UiObject(
				new UiSelector().description("Apps"));

		allAppsButton.clickAndWaitForNewWindow();

		UiObject appsTab = new UiObject(new UiSelector().text("Apps"));

		appsTab.click();

		UiScrollable appViews = new UiScrollable(
				new UiSelector().scrollable(true));

		appViews.setAsHorizontalList();

		UiObject settingsApp = appViews
				.getChildByText(new UiSelector()
						.className(android.widget.TextView.class.getName()),
						"Settings");
		settingsApp.clickAndWaitForNewWindow();

		UiObject settingsValidation = new UiObject(
				new UiSelector().packageName("com.android.settings"));
		assertTrue("Unable to detect Settings", settingsValidation.exists());
	}
}
