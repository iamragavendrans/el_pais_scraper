@ElPaisScraper
Feature: El Pais Opinion Article Scraper and Translator

  Background:
    Given I launch the El Pais website

  @language-check
  Scenario: Verify El Pais site is in Spanish
    Given I verify the El Pais website is in Spanish