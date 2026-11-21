// For the test: the top and bottom halves where they sit assembled. The intersection is empty
// while the halves close without running into each other.
use <../transistor_tester.scad>

intersection() {
    top();
    bot();
}
