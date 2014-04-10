package com.uia.example.my;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class LaunchGooglePlay extends UiAutomatorTestCase {

	public void testDemo() throws UiObjectNotFoundException {

		getUiDevice().pressHome();
		
		UiObject allAppsButton = new UiObject(new UiSelector().className(android.view.View.class).index(4))
			.getChild(new UiSelector().className(android.widget.TextView.class).index(2));
		allAppsButton.click();

		UiObject googlePlayIcon = new UiObject(new UiSelector().description("Shop"));
		googlePlayIcon.click();

		UiObject playStoreText = new UiObject(new UiSelector().text("Play Store"));
		assertTrue("Play Store Text does not exist.", playStoreText.waitForExists(5000));
	}
}