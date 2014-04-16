package com.uia.example.my;

import com.android.uiautomator.testrunner.IAutomationSupport;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class TransferVariables extends UiAutomatorTestCase {

	@Override
	public IAutomationSupport getAutomationSupport() {
		// TODO Auto-generated method stub
		return super.getAutomationSupport();
	}

	public void testDemo() {
		String a = getParams().getString("appName");
		System.out.println(a);
//		getAutomationSupport().sendStatus(arg0, arg1);
	}
}