from typing import Dict, List, Optional, Tuple, Any
import pandas as pd
import numpy as np


class PandasExercises:
    """
    Pandas exercises for data manipulation and analysis.
    
    Pandas is essential for:
    - Data cleaning and preprocessing
    - Exploratory data analysis (EDA)
    - Data transformation and aggregation
    - Time series analysis
    - Data I/O operations
    
    Key concepts:
    - Series and DataFrame
    - Indexing and selection
    - GroupBy operations
    - Merging and joining
    - Data cleaning techniques
    """
    
    # BASIC EXERCISES - DataFrame and Series fundamentals
    
    def create_dataframes_basic(self) -> Dict[str, pd.DataFrame]:
        """
        Basic: Create DataFrames using various methods.
        
        Practice creating DataFrames from:
        - Dictionaries
        - Lists of lists
        - NumPy arrays
        - CSV data (simulated)
        - Random data
        
        TODO: Create and return different types of DataFrames
        """
        result = {}
        
        # Create from dictionary
        # data_dict = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
        # result['from_dict'] = ...
        
        # Create from list of lists
        # data_list = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
        # result['from_list'] = ...
        
        # Create from NumPy array
        # arr = np.random.rand(5, 3)
        # result['from_numpy'] = ...
        
        # Create with custom index
        # result['custom_index'] = ...
        
        # Create with datetime index
        # dates = pd.date_range('2023-01-01', periods=10)
        # result['with_dates'] = ...
        
        return result
    
    def series_operations(self) -> Dict[str, pd.Series]:
        """
        Basic: Practice Series operations and methods.
        
        Series operations:
        - Creation and indexing
        - Mathematical operations
        - String operations
        - Boolean indexing
        - Statistical methods
        
        TODO: Demonstrate various Series operations
        """
        result = {}
        
        # Create Series
        # s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
        
        # Basic operations
        # result['doubled'] = ...
        # result['squared'] = ...
        # result['greater_than_3'] = ...
        
        # String Series operations
        # text_series = pd.Series(['hello', 'world', 'pandas', 'python'])
        # result['uppercase'] = ...
        # result['contains_p'] = ...
        
        return result
    
    def dataframe_indexing(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Basic: Practice DataFrame indexing and selection.
        
        Indexing methods:
        - Column selection
        - Row selection with iloc/loc
        - Boolean indexing
        - Query method
        - Multi-indexing basics
        
        TODO: Implement various indexing operations
        """
        result = {}
        
        # Select single column
        # result['single_column'] = ...
        
        # Select multiple columns
        # result['multiple_columns'] = ...
        
        # Select rows by position
        # result['first_3_rows'] = ...
        
        # Select rows by condition
        # result['conditional_rows'] = ...
        
        # Use query method
        # result['query_result'] = ...
        
        return result
    
    # INTERMEDIATE EXERCISES - Data manipulation and cleaning
    
    def data_cleaning_operations(self, df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """
        Intermediate: Practice data cleaning techniques.
        
        Cleaning operations:
        - Handling missing values
        - Removing duplicates
        - Data type conversions
        - Outlier detection and treatment
        - String cleaning
        
        TODO: Implement comprehensive data cleaning
        """
        result = {}
        
        # Handle missing values
        # result['drop_na'] = ...
        # result['fill_na'] = ...
        # result['interpolate'] = ...
        
        # Remove duplicates
        # result['drop_duplicates'] = ...
        
        # Convert data types
        # result['converted_types'] = ...
        
        # Detect outliers using IQR
        # result['no_outliers'] = ...
        
        return result
    
    def groupby_operations(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Intermediate: Practice GroupBy operations.
        
        GroupBy techniques:
        - Basic aggregations
        - Multiple aggregation functions
        - Custom aggregations
        - Transform operations
        - Apply custom functions
        
        TODO: Implement various GroupBy operations
        """
        result = {}
        
        # Basic groupby aggregation
        # result['group_mean'] = ...
        # result['group_sum'] = ...
        
        # Multiple aggregations
        # result['multiple_aggs'] = ...
        
        # Custom aggregation
        # result['custom_agg'] = ...
        
        # Transform operations
        # result['normalized'] = ...
        
        # Apply custom function
        # result['custom_apply'] = ...
        
        return result
    
    def merging_joining(self) -> Dict[str, pd.DataFrame]:
        """
        Intermediate: Practice merging and joining DataFrames.
        
        Join operations:
        - Inner join
        - Left/right/outer joins
        - Concatenation
        - Index-based joins
        - Multiple key joins
        
        TODO: Demonstrate various join operations
        """
        result = {}
        
        # Create sample DataFrames
        # df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
        # df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
        
        # Different types of joins
        # result['inner_join'] = ...
        # result['left_join'] = ...
        # result['outer_join'] = ...
        
        # Concatenation
        # result['concat_rows'] = ...
        # result['concat_cols'] = ...
        
        return result
    
    # ADVANCED EXERCISES - Complex data analysis
    
    def pivot_and_reshape(self, df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """
        Advanced: Practice data reshaping and pivot operations.
        
        Reshaping operations:
        - Pivot tables
        - Melt operations
        - Stack/unstack
        - Cross-tabulation
        - Wide to long format conversion
        
        TODO: Implement data reshaping operations
        """
        result = {}
        
        # Create pivot table
        # result['pivot_table'] = ...
        
        # Melt DataFrame
        # result['melted'] = ...
        
        # Stack/unstack operations
        # result['stacked'] = ...
        # result['unstacked'] = ...
        
        # Cross-tabulation
        # result['crosstab'] = ...
        
        return result
    
    def time_series_operations(self) -> Dict[str, Any]:
        """
        Advanced: Practice time series analysis with Pandas.
        
        Time series operations:
        - Date/time indexing
        - Resampling
        - Rolling windows
        - Time zone handling
        - Seasonal decomposition
        
        TODO: Implement time series analysis
        """
        result = {}
        
        # Create time series data
        # dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
        # ts = pd.Series(np.random.randn(len(dates)), index=dates)
        
        # Resampling
        # result['monthly_mean'] = ...
        # result['weekly_sum'] = ...
        
        # Rolling operations
        # result['rolling_mean'] = ...
        # result['rolling_std'] = ...
        
        # Date operations
        # result['month_filter'] = ...
        # result['day_of_week'] = ...
        
        return result
    
    def advanced_aggregations(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Advanced: Complex aggregation and window functions.
        
        Advanced techniques:
        - Window functions
        - Cumulative operations
        - Rank operations
        - Quantile calculations
        - Custom aggregation functions
        
        TODO: Implement advanced aggregation techniques
        """
        result = {}
        
        # Window functions
        # result['rank'] = ...
        # result['percent_rank'] = ...
        
        # Cumulative operations
        # result['cumsum'] = ...
        # result['cumprod'] = ...
        
        # Quantile operations
        # result['quantiles'] = ...
        
        # Custom aggregations
        # result['custom_stats'] = ...
        
        return result
    
    # PRACTICAL EXERCISES - Real-world data analysis
    
    def exploratory_data_analysis(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Practical: Comprehensive exploratory data analysis.
        
        EDA components:
        - Dataset overview
        - Statistical summaries
        - Correlation analysis
        - Distribution analysis
        - Missing value analysis
        
        TODO: Perform comprehensive EDA
        """
        result = {}
        
        # Basic info
        # result['shape'] = df.shape
        # result['dtypes'] = df.dtypes
        # result['memory_usage'] = df.memory_usage()
        
        # Statistical summary
        # result['describe'] = ...
        
        # Missing values
        # result['missing_count'] = ...
        # result['missing_percent'] = ...
        
        # Correlation matrix
        # result['correlation'] = ...
        
        # Unique values per column
        # result['unique_counts'] = ...
        
        return result
    
    def feature_engineering(self, df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """
        Practical: Feature engineering techniques.
        
        Feature engineering:
        - Creating new features
        - Binning continuous variables
        - Encoding categorical variables
        - Date/time feature extraction
        - Text feature extraction
        
        TODO: Implement feature engineering techniques
        """
        result = {}
        
        # Create new features
        # result['with_new_features'] = ...
        
        # Binning
        # result['binned'] = ...
        
        # One-hot encoding
        # result['encoded'] = ...
        
        # Date features
        # result['date_features'] = ...
        
        # Text features
        # result['text_features'] = ...
        
        return result
    
    def performance_optimization(self, size: int = 100000) -> Dict[str, Any]:
        """
        Advanced: Pandas performance optimization.
        
        Optimization techniques:
        - Vectorization vs loops
        - Memory efficient data types
        - Chunked processing
        - Query optimization
        - Index optimization
        
        TODO: Demonstrate performance optimization
        """
        import time
        
        result = {}
        
        # Create large DataFrame
        # df = pd.DataFrame({
        #     'A': np.random.randn(size),
        #     'B': np.random.randn(size),
        #     'C': np.random.choice(['X', 'Y', 'Z'], size)
        # })
        
        # Vectorized vs loop performance
        # start_time = time.time()
        # vectorized_result = df['A'] * df['B']
        # vectorized_time = time.time() - start_time
        
        # start_time = time.time()
        # loop_result = df.apply(lambda row: row['A'] * row['B'], axis=1)
        # loop_time = time.time() - start_time
        
        # result['vectorized_time'] = vectorized_time
        # result['loop_time'] = loop_time
        # result['speedup'] = loop_time / vectorized_time
        
        # Memory optimization
        # result['memory_before'] = df.memory_usage(deep=True).sum()
        # df_optimized = df.copy()
        # df_optimized['C'] = df_optimized['C'].astype('category')
        # result['memory_after'] = df_optimized.memory_usage(deep=True).sum()
        
        return result
    
    def data_validation(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Practical: Data validation and quality checks.
        
        Validation checks:
        - Data type validation
        - Range validation
        - Consistency checks
        - Completeness checks
        - Business rule validation
        
        TODO: Implement comprehensive data validation
        """
        result = {}
        
        # Data type checks
        # result['type_errors'] = ...
        
        # Range validation
        # result['range_violations'] = ...
        
        # Duplicates check
        # result['duplicate_count'] = ...
        
        # Consistency checks
        # result['consistency_errors'] = ...
        
        # Completeness
        # result['completeness_score'] = ...
        
        return result