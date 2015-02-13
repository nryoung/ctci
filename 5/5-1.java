/**
 * You are given two 32 bit numbers, N and M, and two bit positions, i and j.
 * Write a method to insert M into N such that M starts at bit j and ends at
 * bit i. You can assume that the bits j through i have enough space to fit all
 * of M. That is, if M = 10011, you can assume that there are at least 5 bits
 * between ja and i. You would not, for example, have j = 3 and i = 2, because
 * M could not fully fit between bit 3 and bit 2.
 *
 * EXAMPLE:
 *
 * Input: N = 10000000000, M = 10011, i = 2, j = 6
 * Output: N = 10001001100
 *
 * ANSWER:
 * The book claims this is a 3 part process, but I think it is better broken
 * down in these discrete steps.
 *
 * 1) Shift a left mask of ones to position j
 * 2) Shift a right mask of ones to position i
 * 3) Create the final overall mask
 * 4) In N clear the bits j -> i with the mask
 * 5) Shift M to the correct starting position (i) in this case
 * 6) Finally apply OR together n_cleared and m_shifted to get the modified M
 **/

class UpdateBits {
    static int updateBits(int n, int m, int i, int j) {
        /* Create a mask to clear bits i through j in n
         * Example: i = 2, j = 4. Result should be 11100011
         * For simplicity, we'll use just 8 bits for the example
         */
        int allOnes = ~0; // will equal sequence of all 1's

        // 1's before position j, then 0's. left = 11100000
        int left = allOnes << (j + 1);

        // 1's after position i. right = 00000011
        int right = ((1 << i) - 1);

        // All 1's, excet for 0's between j and i. mask = 11100011
        // Uses a bitwise inclusive OR
        int mask = left | right;

        /* Clear bits j through i then put m in there */
        int n_cleared = n & mask; // Clear bits j through i.
        int m_shifted = m << i; // Move m into correct position.

        return n_cleared | m_shifted; // OR them, and we're done!
    }
}

class TestUpdateBits {
    public static void main(String[] args) {
        int N = 0b1000000000;
        int M = 0b10011;
        int i = 2;
        int j = 6;
        int output = UpdateBits.updateBits(N, M, i, j);
        System.out.println("N is now: " + Integer.toBinaryString(output));
    }

}
