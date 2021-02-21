# Practice Session for OOP

## Animals

Create hierarchy of classes tha

## Temperature class

Create a Temperature class that is initialized by celsius or by farenheight of by kelvin value, and then makes other temperatures available as attributes.

```python
temp_1 = Temperature(celsius=37.0)
temp_2 = Temperature(fahrenheit=98.6)

print(temp_1.fahrenheit) -> 98.6
print(temp_2.celsius) -> 37.0
print(temp_1.kelvin) -> 310.15
print(temp_2.kelvin) -> 310.15
```

## Deck of cards 

Create a Deck of cards class. Internally, the deck of cards should use another class, a Card class. 

Your requirements are:

- On creating new instance of Deck it should fill itself with 52 Cards.
- The Deck class should have a *deal* method to deal a single card from the deck.
- After a card is dealt, it is removed from the deck and returned.
- There should be a *shuffle* method which rearranges Cards within Deck randomly (https://www.w3schools.com/python/ref_random_shuffle.asp)
- There should be a *cards_left* property that returns how many cards left within Deck. 
- The Card class should have a suit [(Heart, Diamond, Club, Spade)](https://www.vecteezy.com/vector-art/600179-gambling-and-symbols-on-various-cards-heart-diamonds-club-and-spade) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
- When deck is empty, it should return None on calling *deal* method.
