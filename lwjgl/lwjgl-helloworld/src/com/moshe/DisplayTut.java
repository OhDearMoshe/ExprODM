package com.moshe;

import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
 
import java.nio.ByteBuffer;
 
import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.system.MemoryUtil.*;

public class DisplayTut {

	private GLFWErrorCallback errorCallback = GLFWErrorCallback.createPrint(System.err);
	private GLFWKeyCallback keyCallback = new GLFWKeyCallback() {
	    @Override
	    public void invoke(long window, int key, int scancode, int action, int mods) {
	        if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS) {
	            glfwSetWindowShouldClose(window, GLFW_TRUE);
	        }
	    }
	};
	
	private long window;
	
	public void start(){
		glfwSetErrorCallback(errorCallback);
		if (glfwInit() != GLFW_TRUE) {
		    throw new IllegalStateException("Unable to initialize GLFW");
		}
		
		long window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL);
		if (window == NULL) {
		    glfwTerminate();
		    throw new RuntimeException("Failed to create the GLFW window");
		}
		glfwSetKeyCallback(window, keyCallback);
		glfwMakeContextCurrent(window);
		GL.createCapabilities();
		
		while (glfwWindowShouldClose(window) != GLFW_TRUE) {
			double time = glfwGetTime();
			glfwSwapBuffers(window);
			glfwPollEvents();
		}
		
		glfwDestroyWindow(window);
		keyCallback.release();
		glfwTerminate();
		errorCallback.release();
		
	}
	
	public static void main(String[] argv){
		DisplayTut displayTut = new DisplayTut();
		displayTut.start();
	}
}
