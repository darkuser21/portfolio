export declare const MIGRATION_DIR_PATTERN: RegExp;
interface ValidationError {
    type: 'invalid_dir_name' | 'missing_sql_file';
    dirName: string;
}
interface ValidationResult {
    valid: true;
    dirs: string[];
}
interface ValidationFailure {
    valid: false;
    errors: ValidationError[];
}
export declare const validateMigrationDirs: (dirNames: string[], existingSqlFiles: Set<string>) => ValidationResult | ValidationFailure;
export declare const formatValidationErrors: (errors: ValidationError[]) => string;
export {};
