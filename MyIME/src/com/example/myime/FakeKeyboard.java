package com.example.myime;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.inputmethodservice.InputMethodService;
import android.inputmethodservice.KeyboardView;
import android.view.KeyEvent;
import android.view.inputmethod.InputConnection;
import android.widget.Toast;

public class FakeKeyboard extends InputMethodService
        implements KeyboardView.OnKeyboardActionListener {
	
	private static String word = "";
	
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		return super.onKeyDown(keyCode, event);
	}
	
	@Override
	public boolean onKeyUp(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_UNKNOWN) {
			InputConnection ic = getCurrentInputConnection();
			ic.commitText(word, word.length());
			ic.endBatchEdit();
			Toast.makeText(FakeKeyboard.this, word, Toast.LENGTH_SHORT).show();
			// Clear the word
			word = "";
			return true;
		}
		else{
			return super.onKeyUp(keyCode, event);
		}
	}
	
    public static class MyIntentReceiver extends BroadcastReceiver {
    	
    	@Override
    	public void onReceive(Context context, Intent intent) {
    		if(intent.getAction().equals("myIME.intent.action.pass.string")){
    			// Get the unicode from intent
    			String inputString = intent.getStringExtra("input");
    			// Transfer unicode to string
    			word = unicode2Str(inputString);
    		}
    	}
    	
    	public static String str2Unicode(String str) {
    		StringBuffer sb = new StringBuffer();
    		char[] charArr = str.toCharArray();
    		for (char ch : charArr) {
    			if (ch > 128) {
    				sb.append("\\u" + Integer.toHexString(ch));
    			} else {
    				sb.append(ch);
    			}
    		}
    		return sb.toString();
    	}
    	
    	public static String unicode2Str(String str) {
    		StringBuffer sb = new StringBuffer();
    		String[] arr = str.split("\\\\u");
    		int len = arr.length;
    		sb.append(arr[0]);
    		for(int i=1; i<len; i++){
    			String tmp = arr[i];
    			char c = (char)Integer.parseInt(tmp.substring(0, 4), 16);
    			sb.append(c);
    			sb.append(tmp.substring(4));
    		}
    		return sb.toString();
    	}
    }

	//implements KeyboardView.OnKeyboardActionListener
	@Override
	public void onKey(int arg0, int[] arg1) {
	}

	@Override
	public void onPress(int arg0) {
	}

	@Override
	public void onRelease(int arg0) {
	}

	@Override
	public void onText(CharSequence arg0) {
	}

	@Override
	public void swipeDown() {
	}

	@Override
	public void swipeLeft() {
	}

	@Override
	public void swipeRight() {
	}

	@Override
	public void swipeUp() {
	}

}
