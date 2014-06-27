package com.uia.example.my;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class Operation extends UiAutomatorTestCase {

	public void testOperation() {
		UiObject zero = new UiObject(new UiSelector().text("0"));
		UiObject one = new UiObject(new UiSelector().text("1"));
//		UiObject two = new UiObject(new UiSelector().text("2"));
//		UiObject three = new UiObject(new UiSelector().text("3"));
//		UiObject four = new UiObject(new UiSelector().text("4"));
//		UiObject five = new UiObject(new UiSelector().text("5"));
//		UiObject six = new UiObject(new UiSelector().text("6"));
//		UiObject seven = new UiObject(new UiSelector().text("7"));
//		UiObject eight = new UiObject(new UiSelector().text("8"));
//		UiObject nine = new UiObject(new UiSelector().text("9"));
		try {
			zero.click();
			one.click();
//			two.click();
//			three.click();
//			four.click();
//			five.click();
//			six.click();
//			seven.click();
//			eight.click();
//			nine.click();
		} catch (UiObjectNotFoundException e) {
			e.printStackTrace();
		}
	}
}

//uiautomator runtest Uiautomator.jar -c com.uia.example.my.Operation