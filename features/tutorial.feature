Feature: showing off behave

  Scenario: Sprawdzenie zachowania napięcia na baterii 1.5V AA w lampce
    Given Ustaw tryb pomiaru na: AUTO
    And Ustaw odczyt napięcia stałego dla urządzenia Miernik Rigol
    When Zmierz wartości: VDC dla urządzenia: Miernik Rigol przez 1 min co 2 sek i zapisz do pliku: testy.txt
    Then Wyrysuj wykres ze zmiennych z pliku: testy.txt

