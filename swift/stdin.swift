//Script to read stdin line by line, transform, and return it

import Foundation

var i = 1

while let user_input = readLine() {
    print("\(i) \(user_input.uppercased())")
    i += 1
}
