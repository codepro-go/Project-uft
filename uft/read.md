Welcome to Py4J
Py4J enables Python programs running in a Python interpreter to dynamically access Java objects in a Java Virtual Machine. Methods are called as if the Java objects resided in the Python interpreter and Java collections can be accessed through standard Python collection methods. Py4J also enables Java programs to call back Python objects. Py4J is distributed under the BSD license.

Here is a brief example of what you can do with Py4J. The following Python program creates a java.util.Random instance from a JVM and calls some of its methods. It also accesses a custom Java class, AdditionApplication to add the generated numbers.

>>> from py4j.java_gateway import JavaGateway
>>> gateway = JavaGateway()                   # connect to the JVM
>>> random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
>>> number1 = random.nextInt(10)              # call the Random.nextInt method
>>> number2 = random.nextInt(10)
>>> print(number1, number2)
(2, 7)
>>> addition_app = gateway.entry_point               # get the AdditionApplication instance
>>> value = addition_app.addition(number1, number2) # call the addition method
>>> print(value)
9
This is the Java program that was executing at the same time (no code was generated and no tool was required to run these programs). The AdditionApplication app instance is the gateway.entry_point in the previous code snippet. Note that the Java program must be started before executing the Python code above. In other words, the Py4J does not start a JVM.

import py4j.GatewayServer;

public class AdditionApplication {

  public int addition(int first, int second) {
    return first + second;
  }

  public static void main(String[] args) {
    AdditionApplication app = new AdditionApplication();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
  }
}
Support & Resources
Take a look at the tutorial Getting Started with Py4J.

Browse the Py4J Documentation or the Frequently Asked Questions.

Ask a question on the mailing list.

Look at the roadmap.

Request professional services for custom features or commercial support.
