from typing import Tuple, List, Optional
import numpy as np


class NumpyExercises:
    """
    NumPy exercises for scientific computing and data manipulation.
    
    NumPy is the foundation of the Python scientific computing ecosystem.
    Essential for:
    - Numerical computations
    - Array operations
    - Linear algebra
    - Data preprocessing for ML
    - Performance-critical calculations
    
    Key concepts:
    - N-dimensional arrays (ndarray)
    - Broadcasting
    - Vectorization
    - Universal functions (ufuncs)
    - Memory layout and performance
    """
    
    # BASIC EXERCISES - Array creation and manipulation
    
    def create_arrays_basic(self) -> dict:
        """
        Basic: Create various types of NumPy arrays.
        
        Practice creating:
        - Arrays from lists
        - Zeros, ones, empty arrays
        - Arrays with specific ranges
        - Identity matrices
        - Random arrays
        
        TODO: Create and return dictionary with different array types
        """
        result = {}
        
        # Create array from list
        # result['from_list'] = ...
        
        # Create zeros array of shape (3, 4)
        # result['zeros'] = ...
        
        # Create ones array of shape (2, 3)
        # result['ones'] = ...
        
        # Create array with range 0 to 9
        # result['range'] = ...
        
        # Create 3x3 identity matrix
        # result['identity'] = ...
        
        # Create random array of shape (2, 2)
        # result['random'] = ...
        
        return result
    
    def array_indexing_slicing(self, arr: np.ndarray) -> dict:
        """
        Basic: Practice array indexing and slicing.
        
        Given a 2D array, extract:
        - Single element
        - Entire row
        - Entire column
        - Subarray
        - Elements using boolean indexing
        
        TODO: Implement various indexing operations
        """
        result = {}
        
        # Get element at position (0, 1)
        # result['element'] = ...
        
        # Get first row
        # result['first_row'] = ...
        
        # Get second column
        # result['second_col'] = ...
        
        # Get 2x2 subarray from top-left
        # result['subarray'] = ...
        
        # Get elements greater than mean
        # result['greater_than_mean'] = ...
        
        return result
    
    def array_operations_basic(self, arr1: np.ndarray, arr2: np.ndarray) -> dict:
        """
        Basic: Practice basic array operations.
        
        Given two arrays, perform:
        - Element-wise arithmetic
        - Matrix multiplication
        - Statistical operations
        - Shape manipulations
        
        TODO: Implement basic array operations
        """
        result = {}
        
        # Element-wise addition
        # result['add'] = ...
        
        # Element-wise multiplication
        # result['multiply'] = ...
        
        # Matrix multiplication (if shapes allow)
        # result['matmul'] = ...
        
        # Sum along axis 0
        # result['sum_axis0'] = ...
        
        # Reshape array to different shape
        # result['reshaped'] = ...
        
        return result
    
    # INTERMEDIATE EXERCISES - Broadcasting and advanced operations
    
    def broadcasting_exercises(self) -> dict:
        """
        Intermediate: Practice NumPy broadcasting.
        
        Broadcasting allows operations on arrays with different shapes:
        - Scalar with array
        - 1D with 2D arrays
        - Adding arrays with compatible dimensions
        
        TODO: Demonstrate broadcasting with various array combinations
        """
        result = {}
        
        # Create arrays for broadcasting examples
        # scalar = 5
        # arr_1d = np.array([1, 2, 3])
        # arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
        
        # Scalar + 2D array
        # result['scalar_plus_2d'] = ...
        
        # 1D + 2D array (broadcast along rows)
        # result['1d_plus_2d'] = ...
        
        # Transpose and broadcast
        # result['transpose_broadcast'] = ...
        
        return result
    
    def vectorization_vs_loops(self, size: int = 10000) -> dict:
        """
        Intermediate: Compare vectorized operations vs Python loops.
        
        Demonstrate why vectorization is faster:
        - Compute squares using loops vs NumPy
        - Measure performance difference
        - Show memory efficiency
        
        TODO: Implement both approaches and compare performance
        """
        import time
        
        result = {}
        
        # Create test array
        # arr = np.random.rand(size)
        
        # Method 1: Python loop
        # start_time = time.time()
        # loop_result = [x**2 for x in arr]
        # loop_time = time.time() - start_time
        
        # Method 2: NumPy vectorization
        # start_time = time.time()
        # vectorized_result = arr**2
        # vectorized_time = time.time() - start_time
        
        # result['loop_time'] = loop_time
        # result['vectorized_time'] = vectorized_time
        # result['speedup'] = loop_time / vectorized_time
        
        return result
    
    def universal_functions(self, arr: np.ndarray) -> dict:
        """
        Intermediate: Practice universal functions (ufuncs).
        
        Ufuncs operate element-wise on arrays:
        - Mathematical functions
        - Trigonometric functions
        - Logical functions
        - Custom ufuncs
        
        TODO: Apply various ufuncs to input array
        """
        result = {}
        
        # Mathematical ufuncs
        # result['sqrt'] = ...
        # result['exp'] = ...
        # result['log'] = ...
        
        # Trigonometric ufuncs
        # result['sin'] = ...
        # result['cos'] = ...
        
        # Logical ufuncs
        # result['greater_than_mean'] = ...
        # result['is_positive'] = ...
        
        return result
    
    # ADVANCED EXERCISES - Linear algebra and performance optimization
    
    def linear_algebra_operations(self) -> dict:
        """
        Advanced: Practice linear algebra with NumPy.
        
        Essential operations:
        - Matrix multiplication
        - Eigenvalues and eigenvectors
        - Matrix decompositions
        - Solving linear systems
        - Matrix inverse and determinant
        
        TODO: Implement linear algebra operations
        """
        result = {}
        
        # Create sample matrices
        # A = np.random.rand(3, 3)
        # B = np.random.rand(3, 3)
        # b = np.random.rand(3)
        
        # Matrix multiplication
        # result['matmul'] = ...
        
        # Eigenvalues and eigenvectors
        # eigenvals, eigenvecs = np.linalg.eig(A)
        # result['eigenvals'] = eigenvals
        # result['eigenvecs'] = eigenvecs
        
        # Solve linear system Ax = b
        # result['solve'] = ...
        
        # Matrix inverse
        # result['inverse'] = ...
        
        # Determinant
        # result['det'] = ...
        
        return result
    
    def advanced_array_manipulation(self, data: np.ndarray) -> dict:
        """
        Advanced: Complex array manipulation techniques.
        
        Techniques:
        - Fancy indexing
        - Array concatenation and splitting
        - Structured arrays
        - Memory views and copies
        - Advanced slicing
        
        TODO: Implement advanced manipulation techniques
        """
        result = {}
        
        # Fancy indexing
        # indices = np.array([0, 2, 4])
        # result['fancy_index'] = ...
        
        # Array concatenation
        # result['concatenated'] = ...
        
        # Array splitting
        # result['split'] = ...
        
        # Unique elements and counts
        # unique_vals, counts = np.unique(data, return_counts=True)
        # result['unique'] = unique_vals
        # result['counts'] = counts
        
        return result
    
    def performance_optimization(self, size: int = 1000000) -> dict:
        """
        Advanced: NumPy performance optimization techniques.
        
        Optimization strategies:
        - Memory layout (C vs Fortran order)
        - In-place operations
        - Avoiding copies
        - Using views efficiently
        - Numba integration concepts
        
        TODO: Demonstrate performance optimization techniques
        """
        import time
        
        result = {}
        
        # Create test arrays
        # arr_c = np.random.rand(1000, 1000)  # C order
        # arr_f = np.asfortranarray(arr_c)    # Fortran order
        
        # Compare row vs column access performance
        # Row access (C order efficient)
        # start_time = time.time()
        # row_sum = np.sum(arr_c, axis=1)
        # c_row_time = time.time() - start_time
        
        # Column access (Fortran order efficient)
        # start_time = time.time()
        # col_sum = np.sum(arr_f, axis=0)
        # f_col_time = time.time() - start_time
        
        # In-place vs copy operations
        # arr_copy = arr_c.copy()
        # start_time = time.time()
        # arr_copy += 1  # In-place
        # inplace_time = time.time() - start_time
        
        # start_time = time.time()
        # new_arr = arr_c + 1  # Creates copy
        # copy_time = time.time() - start_time
        
        # result['c_row_time'] = c_row_time
        # result['f_col_time'] = f_col_time
        # result['inplace_time'] = inplace_time
        # result['copy_time'] = copy_time
        
        return result
    
    # DATA SCIENCE EXERCISES - Practical applications
    
    def statistical_analysis(self, data: np.ndarray) -> dict:
        """
        Practical: Statistical analysis of data.
        
        Common statistics:
        - Descriptive statistics
        - Correlation analysis
        - Percentiles and quantiles
        - Outlier detection
        - Distribution fitting
        
        TODO: Compute comprehensive statistical analysis
        """
        result = {}
        
        # Basic statistics
        # result['mean'] = ...
        # result['std'] = ...
        # result['median'] = ...
        # result['min'] = ...
        # result['max'] = ...
        
        # Percentiles
        # result['q25'] = ...
        # result['q75'] = ...
        
        # Outlier detection (using IQR method)
        # q1, q3 = np.percentile(data, [25, 75])
        # iqr = q3 - q1
        # outlier_mask = (data < q1 - 1.5*iqr) | (data > q3 + 1.5*iqr)
        # result['outliers'] = data[outlier_mask]
        
        return result
    
    def image_processing_basics(self, image_shape: Tuple[int, int, int] = (100, 100, 3)) -> dict:
        """
        Practical: Basic image processing with NumPy.
        
        Image operations:
        - Creating synthetic images
        - Color channel manipulation
        - Basic filters
        - Geometric transformations
        - Histogram analysis
        
        TODO: Implement basic image processing operations
        """
        result = {}
        
        # Create random image
        # image = np.random.randint(0, 256, image_shape, dtype=np.uint8)
        
        # Extract color channels
        # result['red_channel'] = ...
        # result['green_channel'] = ...
        # result['blue_channel'] = ...
        
        # Convert to grayscale
        # result['grayscale'] = ...
        
        # Apply simple blur (average of neighbors)
        # result['blurred'] = ...
        
        # Image histogram
        # result['histogram'] = ...
        
        return result
    
    def time_series_analysis(self, days: int = 365) -> dict:
        """
        Practical: Time series analysis with NumPy.
        
        Time series operations:
        - Generate synthetic time series
        - Moving averages
        - Trend analysis
        - Seasonal decomposition
        - Autocorrelation
        
        TODO: Implement time series analysis functions
        """
        result = {}
        
        # Generate synthetic time series
        # t = np.arange(days)
        # trend = 0.1 * t
        # seasonal = 10 * np.sin(2 * np.pi * t / 365.25)
        # noise = np.random.normal(0, 1, days)
        # ts = trend + seasonal + noise
        
        # Moving average
        # window = 30
        # result['moving_avg'] = ...
        
        # Detrend the series
        # result['detrended'] = ...
        
        # Find peaks and valleys
        # result['peaks'] = ...
        # result['valleys'] = ...
        
        return result