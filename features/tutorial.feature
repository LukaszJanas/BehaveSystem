Feature: showing off behave

  Scenario: Test 0
    Given Set load method: "ConstantCurrent" for Itech
    And Set: "Current" to: "1" for Itech
    And Set the type: "Automatic" for measurement: "VAC" for Rigol
    When Turn "On" Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "2" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "3" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "4" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "5" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "6" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "7" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "8" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "9" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Set: "Current" to: "10" for Itech
    And Wait 2s
    Then Read the "AC" voltage from the "Rigol"
    When Turn "Off" Itech

  Scenario: Test 1 - Pomiar prądu przy zadanej mocy ładowania - MEE 1kW
    Given Set the type: "Automatic" for measurement: "VAC" for Rigol
    And Setting all phases for Chroma
    And Set the AC voltage amplitude: "210" V for Chroma
    When Turn "On" Chroma Output
    And Wait 30s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "220" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "230" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "240" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "250" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"

  Scenario: Test 2 - Pomiar mocy i PF przy zadanej mocy ładowania - MEE 1kW
    Given Set the type: "Automatic" for measurement: "VAC" for Rigol
    And Setting all phases for Chroma
    And Set the AC voltage amplitude: "210" V for Chroma
    When Turn "On" Chroma Output
    And Wait 30s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "220" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "230" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "240" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "250" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma

  Scenario: Test 3 - Pomiar prądu przy zadanej mocy rozładowania - MEE -1kW
    Given Set load method: "ConstantPower" for Itech
    And Set: "Power" to: "1500" for Itech
    And Set the type: "Automatic" for measurement: "VAC" for Rigol
    And Setting all phases for Chroma
    When Set the AC voltage amplitude: "210" V for Chroma
    And Turn "On" Itech
    And Turn "On" Chroma Output
    And Wait 30s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "220" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "230" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "240" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    When Set the AC voltage amplitude: "250" V for Chroma
    And Wait 25s
    Then Read the "AC" voltage from the "Rigol"
    
  Scenario: Test 4 - Pomiar mocy i PF przy zadanej mocy rozładowania- MEE -1kW
    Given Set load method: "ConstantPower" for Itech
    And Set: "Power" to: "1500" for Itech
    And Set the type: "Automatic" for measurement: "VAC" for Rigol
    And Setting all phases for Chroma
    When Set the AC voltage amplitude: "210" V for Chroma
    And Turn "On" Itech
    And Turn "On" Chroma Output
    And Wait 30s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "220" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "230" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "240" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma
    When Set the AC voltage amplitude: "250" V for Chroma
    And Wait 25s
    Then Measure 3-phase "real" power for Chroma
    And Measure 3-phase "apparent" power for Chroma
    And Measure power factor for Chroma

  Scenario: Test 5 - Test pracy przy asymetrycznym napięciu i symetrycznym obciążeniu
    Given Set load method: "ConstantPower" for Itech
    And Set: "Power" to: "1500" for Itech
    And Set the AC voltage amplitude: "210" V for the phase "A" for Chroma
    And Set the AC voltage amplitude: "220" V for the phase "B" for Chroma
    And Set the AC voltage amplitude: "230" V for the phase "C" for Chroma
    When Turn "On" Itech
    And Wait 1s
    And Turn "On" Chroma Output
    And Wait 30s
    Then Measure 3-phase "real" power for Chroma