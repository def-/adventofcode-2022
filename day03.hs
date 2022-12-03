#!/usr/bin/env runhaskell
import Data.Char
import Data.List
prio c | c >= 'a' = ord c - ord 'a' + 1 | otherwise = ord c - ord 'A' + 27
split l = splitAt (length l `div` 2) l
slice (x:y:z:xs) = (x,y,z) : slice xs
slice [] = []
part1 = sum . map (prio . head . uncurry intersect . split)
part2 = sum . map (\(x,y,z) -> prio $ head $ intersect x (intersect y z)) . slice
main = do
  ls <- fmap lines $ readFile "day03.in"
  print $ part1 ls
  print $ part2 ls
