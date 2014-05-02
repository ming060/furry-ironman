package com.uia.example.my;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class Operation extends UiAutomatorTestCase {

	public void testOperation() {
		UiObject zero = new UiObject(new UiSelector().text("0"));
		UiObject one = new UiObject(new UiSelector().text("1"));
		try {
			zero.click();
			one.click();
		} catch (UiObjectNotFoundException e) {
			e.printStackTrace();
		}
	}
}