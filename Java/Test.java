package testing;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test {
    public static void main(String[] args) throws IOException, InterruptedException {
        long startTime = System.currentTimeMillis();

        ProcessBuilder pb = new ProcessBuilder(
                "java",
                "-jar",
                "Path_to_jar",
                "Path_to_class"
            );

        Process process = pb.start();
        int exitCode = process.waitFor();

        long endTime = System.currentTimeMillis();

        if (exitCode == 0) {
            System.out.println("Formátovanie dokončené úspešne.");
        } else {
            System.out.println("Formátovanie zlyhalo. Kód ukončenia: " + exitCode);
        }

        System.out.println("Formátovanie trvalo " + (endTime - startTime) + " ms.");
    }
}
