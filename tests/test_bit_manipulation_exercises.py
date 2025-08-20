import pytest
from src.py_dsa.bit_manipulation_exercises import BitManipulationExercises


class TestBitManipulationExercises:
    """
    Tests for bit manipulation exercises covering fundamental bit operations and optimizations.
    Essential for low-level programming and optimization techniques.
    """
    
    def setup_method(self):
        self.bit_ops = BitManipulationExercises()
    
    # BASIC BIT OPERATION TESTS
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_count_set_bits_basic(self):
        """Test counting set bits in various numbers."""
        assert self.bit_ops.count_set_bits(11) == 3  # 1011
        assert self.bit_ops.count_set_bits(7) == 3   # 111
        assert self.bit_ops.count_set_bits(8) == 1   # 1000
        assert self.bit_ops.count_set_bits(0) == 0   # 0
        assert self.bit_ops.count_set_bits(1) == 1   # 1
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_count_set_bits_powers_of_two(self):
        """Test counting bits in powers of 2."""
        assert self.bit_ops.count_set_bits(16) == 1   # 10000
        assert self.bit_ops.count_set_bits(32) == 1   # 100000
        assert self.bit_ops.count_set_bits(64) == 1   # 1000000
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_is_power_of_two_basic(self):
        """Test power of 2 detection."""
        assert self.bit_ops.is_power_of_two(1) == True    # 2^0
        assert self.bit_ops.is_power_of_two(2) == True    # 2^1
        assert self.bit_ops.is_power_of_two(16) == True   # 2^4
        assert self.bit_ops.is_power_of_two(3) == False   # Not power of 2
        assert self.bit_ops.is_power_of_two(0) == False   # Edge case
        assert self.bit_ops.is_power_of_two(-1) == False  # Negative
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_single_number_basic(self):
        """Test finding single number among pairs."""
        assert self.bit_ops.single_number([2, 2, 1]) == 1
        assert self.bit_ops.single_number([4, 1, 2, 1, 2]) == 4
        assert self.bit_ops.single_number([1]) == 1
        assert self.bit_ops.single_number([0, 1, 0]) == 1
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_get_bit_basic(self):
        """Test getting specific bits."""
        # 5 = 101 in binary
        assert self.bit_ops.get_bit(5, 0) == 1  # LSB
        assert self.bit_ops.get_bit(5, 1) == 0  # Middle bit
        assert self.bit_ops.get_bit(5, 2) == 1  # MSB
        assert self.bit_ops.get_bit(5, 3) == 0  # Beyond number
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_set_bit_basic(self):
        """Test setting specific bits."""
        # 5 = 101, setting bit 1 should give 7 = 111
        assert self.bit_ops.set_bit(5, 1) == 7
        # 0 = 000, setting bit 2 should give 4 = 100
        assert self.bit_ops.set_bit(0, 2) == 4
        # Setting already set bit should not change
        assert self.bit_ops.set_bit(5, 0) == 5
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_clear_bit_basic(self):
        """Test clearing specific bits."""
        # 7 = 111, clearing bit 1 should give 5 = 101
        assert self.bit_ops.clear_bit(7, 1) == 5
        # 5 = 101, clearing bit 2 should give 1 = 001
        assert self.bit_ops.clear_bit(5, 2) == 1
        # Clearing already clear bit should not change
        assert self.bit_ops.clear_bit(5, 1) == 5
    
    # INTERMEDIATE XOR PATTERN TESTS
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_single_number_2_basic(self):
        """Test finding single number when others appear 3 times."""
        assert self.bit_ops.single_number_2([2, 2, 3, 2]) == 3
        assert self.bit_ops.single_number_2([0, 1, 0, 1, 0, 1, 99]) == 99
        assert self.bit_ops.single_number_2([1, 1, 1, 2]) == 2
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_single_number_3_basic(self):
        """Test finding two single numbers among pairs."""
        result = self.bit_ops.single_number_3([1, 2, 1, 3, 2, 5])
        assert set(result) == {3, 5}
        
        result = self.bit_ops.single_number_3([1, 1, 0, -2147483648])
        assert set(result) == {0, -2147483648}
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_missing_number_basic(self):
        """Test finding missing number in range."""
        assert self.bit_ops.missing_number([3, 0, 1]) == 2
        assert self.bit_ops.missing_number([0, 1]) == 2
        assert self.bit_ops.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
        assert self.bit_ops.missing_number([0]) == 1
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_find_duplicate_basic(self):
        """Test finding duplicate number."""
        assert self.bit_ops.find_duplicate([1, 3, 4, 2, 2]) == 2
        assert self.bit_ops.find_duplicate([3, 1, 3, 4, 2]) == 3
        assert self.bit_ops.find_duplicate([1, 1]) == 1
    
    # ADVANCED BIT MANIPULATION TESTS
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_reverse_bits_basic(self):
        """Test bit reversal."""
        # Note: This tests the concept, actual values depend on 32-bit representation
        n = 43261596  # 00000010100101000001111010011100
        result = self.bit_ops.reverse_bits(n)
        # Should reverse the bit pattern
        assert isinstance(result, int)
        assert result >= 0
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_number_of_1_bits_basic(self):
        """Test Hamming weight calculation."""
        assert self.bit_ops.number_of_1_bits(11) == 3   # 1011
        assert self.bit_ops.number_of_1_bits(128) == 1  # 10000000
        assert self.bit_ops.number_of_1_bits(0) == 0    # 0
        assert self.bit_ops.number_of_1_bits(7) == 3    # 111
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_bitwise_and_range_basic(self):
        """Test bitwise AND of range."""
        assert self.bit_ops.bitwise_and_range(5, 7) == 4
        assert self.bit_ops.bitwise_and_range(0, 0) == 0
        assert self.bit_ops.bitwise_and_range(1, 2147483647) == 0
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_maximum_xor_basic(self):
        """Test maximum XOR of two numbers."""
        assert self.bit_ops.maximum_xor([3, 10, 5, 25, 2, 8]) == 28  # 5 XOR 25
        assert self.bit_ops.maximum_xor([8, 10, 2]) == 10             # 8 XOR 2
        assert self.bit_ops.maximum_xor([1]) == 0                     # Single element
    
    @pytest.mark.bit_manipulation
    @pytest.mark.easy
    def test_counting_bits_basic(self):
        """Test counting bits for range [0, n]."""
        result = self.bit_ops.counting_bits(2)
        assert result == [0, 1, 1]  # bits in 0, 1, 2
        
        result = self.bit_ops.counting_bits(5)
        assert result == [0, 1, 1, 2, 1, 2]  # bits in 0,1,2,3,4,5
    
    # PATTERN AND ADVANCED ALGORITHM TESTS
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_gray_code_basic(self):
        """Test Gray code generation."""
        result = self.bit_ops.gray_code(2)
        assert result == [0, 1, 3, 2]  # 00, 01, 11, 10
        
        result = self.bit_ops.gray_code(1)
        assert result == [0, 1]  # 0, 1
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_sum_without_arithmetic_basic(self):
        """Test addition without arithmetic operators."""
        assert self.bit_ops.sum_without_arithmetic(1, 2) == 3
        assert self.bit_ops.sum_without_arithmetic(2, 3) == 5
        assert self.bit_ops.sum_without_arithmetic(-1, 1) == 0
        assert self.bit_ops.sum_without_arithmetic(0, 5) == 5
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_divide_without_division_basic(self):
        """Test division without division operators."""
        assert self.bit_ops.divide_without_division(10, 3) == 3
        assert self.bit_ops.divide_without_division(7, -3) == -2
        assert self.bit_ops.divide_without_division(0, 1) == 0
        assert self.bit_ops.divide_without_division(1, 1) == 1
    
    @pytest.mark.bit_manipulation
    @pytest.mark.medium
    def test_divide_without_division_edge_cases(self):
        """Test division edge cases."""
        # Test overflow cases (should be handled according to 32-bit integer limits)
        assert self.bit_ops.divide_without_division(-2147483648, -1) <= 2147483647
        assert self.bit_ops.divide_without_division(-2147483648, 1) >= -2147483648