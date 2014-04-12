package com.uia.example.my;

import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class TransferVariables extends UiAutomatorTestCase {

	public void testDemo() {
		String a = getParams().getString("appName");
		System.out.println(a);
	}
}