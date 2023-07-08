Feature: showing off behave

  Scenario: Sprawdzenie zachowania napięcia na baterii 1.5V AA w lampce
    # Then Ustaw tryb pomiaru: AUTO dla pomiaru: VDC dla urządzenia Rigol
    # Then Zmierz wartości: VDC dla urządzenia: Rigol przez 2 min co 2 sek i zapisz do pliku: results.txt
    Then Wyrysuj wykres ze zmiennych z pliku: results.txt