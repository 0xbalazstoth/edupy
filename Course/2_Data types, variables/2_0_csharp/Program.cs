using System;
using System.Runtime.InteropServices;

// dotnet new console
// dotnet run

public class Program
{
    public static void Main()
    {
        // Kezdeti értékadás
        object? value = "Hello, World!";
        Console.WriteLine("0x" + GetMemoryAddress(value));
        Console.WriteLine("Type: " + value.GetType());

        Console.WriteLine("\n");

        // Integer értékadás
        value = 10;
        Console.WriteLine("0x" + GetMemoryAddress(value));
        Console.WriteLine("Type: " + value.GetType());

        object other_value = value;
        Console.WriteLine("0x" + GetMemoryAddress(other_value));
        Console.WriteLine("Type: " + other_value.GetType());

        // Érték módosítása
        value = 11;
        Console.WriteLine("0x" + GetMemoryAddress(value));
        Console.WriteLine("Type: " + value.GetType());

        // value törlése a névtérből
        value = null;
        // Console.WriteLine(value); // Hibát okozna

        System.Console.WriteLine("\n");
        // other_value értékének megjelenítése
        Console.WriteLine("0x" + GetMemoryAddress(other_value));
        Console.WriteLine("Type: " + other_value.GetType());
    }

    public static string GetMemoryAddress(object obj)
    {
        // Memória címének kiírása (egyedi referenciaként működik)
        GCHandle handle = GCHandle.Alloc(obj, GCHandleType.Pinned);
        IntPtr address = handle.AddrOfPinnedObject();
        handle.Free();
        return address.ToString("X");
    }
}
