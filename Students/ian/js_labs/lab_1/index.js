/**
 * lab 1
 * 
 * v1:
 * Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
 * 
 * v2:
 * Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
 * 
 * v3:
 * Add support for yards, and inches.
 * 
 * v4:
 * Now we'll ask the user for the distance, the starting units, and the units to convert to.
 * 
 * pick6:
 * Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

*
* rot13
*Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

 */

const readline = require("readline");
const METER = {
  ft: 0.3048,
  mi: 1609.34,
  m: 1,
  km: 0.001,
  yd: 0.9084,
  in: 0.02523,
};

v1 = rl => {
  rl.question("enter feet: ", ft => {
    const meters = (ft * METER["ft"]).toFixed(2);
    console.log("that is ", meters, " meters");
    rl.close();
  });
};

v23 = rl => {
  rl.question("enter feet: ", dis => {
    rl.question("enter the units: ", units => {
      const denom = METER[units] / METER["ft"];
      if (dis && denom) {
        console.log("that is ", (dis / denom).toFixed(2), units);
      } else {
        console.log("error ", dis, denom);
      }
      rl.close();
    });
  });
};
v4 = rl => {
  rl.question("enter distance: ", dis => {
    rl.question("enter from units: ", from_unit => {
      rl.question("enter to units: ", to_unit => {
        if (METER[from_unit] && METER[to_unit]) {
          console.log(
            "that is ",
            (dis / METER[from_unit] / METER[to_unit]).toFixed(2),
            to_unit
          );
        } else console.log("error");
        rl.close();
      });
    });
  });
};

const payout = {
  1: 4,
  2: 7,
  3: 100,
  4: 50000,
  5: 1000000,
  6: 25000000,
};
pick = n =>
  Array(n)
    .fill()
    .map(() => ~~(Math.random() * 100));

countMatches = (a, b) => {
  let i = 0,
    count = 0;
  if (a?.length && a?.length === b?.length) {
    for (; i < a.length; i++) {
      if (a[i] === b[i]) count++;
    }
  }
  return count;
};

playpick = (nPick, nGames) => {
  const price = 2 * nGames;
  let i = 0,
    money = 0;
  for (; i < nGames; i++) {
    money += payout[countMatches(pick(nPick), pick(nPick))] || 0;
  }
  const total = money - price;
  const roi = total / money;
  return { total, roi };
};
pick6 = () => {
  const { total, roi } = playpick(6, 100);
  console.log(
    total > 0 ? "Your payout is " : "You lost ",
    Math.abs(total),
    `your roi is ${~~(roi * 100)}%`
  );
};

rot = (m, rotn = 13) =>
  [...m]
    .map(c => String.fromCharCode(((c.charCodeAt(0) - 97 + rotn) % 26) + 97))
    .join("");
rot13 = rl => {
  rl.question("enter a word: ", word => {
    console.log("word: ", rot(word));
    rl.close();
  });
};
function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  // v1(rl);
  // v23(rl);
  // v4(rl);
  // pick6();
  rot13(rl);
}

main();
