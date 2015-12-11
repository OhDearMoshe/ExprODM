package com.moshe.aspects;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;

import com.moshe.annotations.Shouter;

/*
 * Aspect class that listens for anything with the
 * Shouter annotation
 */
@Aspect
public class AspectFaff {
	@Pointcut(value="execution(public * *())")
	public void publicMethods(){
		
	}
	@Around("publicMethods() && @annotation(shouter)")
	public Object shoutMethod(ProceedingJoinPoint preceedingJoinPoint, Shouter shouter) throws Throwable {
		System.out.println("Class signiture is: " + preceedingJoinPoint.getSignature());
		//DO Stuff
		return preceedingJoinPoint.proceed();
	}
	
}
