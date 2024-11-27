// Java Key Concepts

import java.util.*;
import java.io.*;

public class KeyConcepts {
    public static void main(String[] args) {
        // 1. Basic Syntax
        System.out.println("Hello, Java!"); // Output text
        Scanner scanner = new Scanner(System.in); // Input text
        System.out.print("What is your name? ");
        String name = scanner.nextLine();
        System.out.println("Nice to meet you, " + name + "!");

        // 2. Control Flow
        int x = 10;
        if (x > 5) {
            System.out.println("x is greater than 5");
        } else {
            System.out.println("x is 5 or less");
        }

        for (int i = 0; i < 3; i++) {
            System.out.println("Loop " + i);
        }

        while (x > 0) {
            System.out.println(x);
            x--;
        }

        // 3. Data Structures
        List<Integer> myList = new ArrayList<>(Arrays.asList(1, 2, 3));
        int[] myArray = {4, 5, 6};
        Map<String, Integer> myMap = new HashMap<>();
        myMap.put("a", 1);
        myMap.put("b", 2);
        Set<Integer> mySet = new HashSet<>(Arrays.asList(1, 2, 3, 2)); // Duplicates removed

        System.out.println(myList + " " + Arrays.toString(myArray) + " " + myMap + " " + mySet);

        // Iteration and Mutation - List
        System.out.println("Original list: " + myList);
        for (int i = 0; i < myList.size(); i++) {
            myList.set(i, myList.get(i) * 2); // Mutate each element
        }
        System.out.println("Mutated list: " + myList);

        // Iteration and Mutation - Map
        System.out.println("Original map: " + myMap);
        for (String key : myMap.keySet()) {
            myMap.put(key, myMap.get(key) + 10); // Mutate each value
        }
        System.out.println("Mutated map: " + myMap);

        // 4. Functions (Methods)
        System.out.println("2 + 3 = " + add(2, 3));

        // 5. Modules and Libraries
        System.out.println("Square root of 16 is " + Math.sqrt(16));

        // 6. File Handling
        try {
            FileWriter writer = new FileWriter("example.txt");
            writer.write("Hello, file!");
            writer.close();

            Scanner fileReader = new Scanner(new File("example.txt"));
            while (fileReader.hasNextLine()) {
                System.out.println(fileReader.nextLine());
            }
            fileReader.close();
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }

        // 7. Error and Exception Handling
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("This runs no matter what");
        }

        // 8. Object-Oriented Programming
        Animal dog = new Dog("Rex");
        System.out.println(dog.speak());

        // 9. Working with Data
        String str = "Hello, world!";
        System.out.println(str.substring(0, 5)); // Slicing
        System.out.println(str.toUpperCase()); // Uppercase

        List<Integer> squares = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            squares.add(i * i); // List comprehension equivalent
        }
        System.out.println(squares);
    }

    // Function example
    public static int add(int a, int b) {
        return a + b;
    }
}

// Class examples for Object-Oriented Programming
class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public String speak() {
        return this.name + " makes a noise";
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public String speak() {
        return this.name + " barks";
    }
}

