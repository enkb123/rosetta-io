import Foundation

var i = 1

while let user_input = readLine() {
    print("\(i) \(user_input.uppercased())")
    i += 1
}
