# Movie Theatre
# Problem

# A concession stand at a movie theatre sells two products: popcorn for $7 and soda for $2.50.
# If someone buys both on the same day, they get a bundle price of $9 for the two items.
# A customer can purchase any number of bundles on the same day. Customers can run a tab, and
# when settling the bill, we need to calculate how much they owe using the list of past purchases.

# Provide a function that, given the list of past purchases as input (string “<date>,<item>“)
# returns the amount owed.

# Here is a list of input/output examples:

# > tally( [ "2022-06-01,soda",
#   ] )
# => 2.5

# > tally( [
#     "2021-11-15,popcorn",
#     "2021-11-15,popcorn",
#     "2021-11-15,soda",
#     "2021-11-15,soda",
#   ] )
# => 18

# (7 + 7 + 2 + 2) = 18

# > tally( [
#     "2019-12-29,popcorn",
#     "2020-01-03,popcorn",
#     "2020-01-03,soda",
#     "2020-01-03,soda",
#     "2020-02-22,popcorn",
#     "2020-02-22,soda",
#   ] ) => 27.5

# (7) + (7 + 2 + 2.5) + (7 + 2) = 27.5

# > tally( [
#     "2019-12-29,soda",
#     "2020-01-03,popcorn",
#     "2020-01-03,soda",
#     "2020-01-03,soda",
#     "2020-02-22,popcorn",
#     "2020-02-22,soda",
#  ] ) => 23

# (2.5) + (7 + 2 + 2.5) + (7 + 2) = 23