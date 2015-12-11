package com.moshe;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.FileSystemXmlApplicationContext;

public class SpringFaff {

	
		public static void main(String[] args){
			ApplicationContext appCont = new FileSystemXmlApplicationContext("src/main/resources/aspect-context.xml");
			Words words = (Words) appCont.getBean("words");
			words.helloWorld();
			words.helloMe();
		}
}
