package com.moshe;

import com.moshe.annotations.Shouter;

public class Words {
	@Shouter()
	public void helloWorld(){
		System.out.println("Shouter should be executed above");
	}
	
	@Shouter()
	public void helloMe(){
		System.out.println("Shouter should be executed above");
		helloYou();
	}
	
	@Shouter()
	public void helloYou(){
		System.out.println("Shouter should not be executed above");
	}
}
