package com.uia.example.my;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class Caculator extends UiAutomatorTestCase {

	public void testOperation() {
		UiObject zero = new UiObject(new UiSelector().className(android.widget.ImageButton.class).index(18));
//		UiObject one = new UiObject(new UiSelector().className(android.widget.ImageButton.class).index(13));
//		UiObject two = new UiObject(new UiSelector().className(android.widget.ImageButton.class).index(14));
//		UiObject three = new UiObject(new UiSelector().className(android.widget.ImageButton.class).index(15));
//		UiObject four = new UiObject(new UiSelector().className(android.widget.ImageButton.class).index(9));
//		UiObject five = new UiObject(new UiSelector().className(android.widget.ImageButton.class).index(10));
		try {
			for (int i = 0; i < 80; i++) {
				zero.click();
			}
//			one.click();
//			two.click();
//			three.click();
//			four.click();
//			five.click();
		} catch (UiObjectNotFoundException e) {
			e.printStackTrace();
		}
	}
}

//uiautomator runtest Uiautomator.jar -c com.uia.example.my.Caculator