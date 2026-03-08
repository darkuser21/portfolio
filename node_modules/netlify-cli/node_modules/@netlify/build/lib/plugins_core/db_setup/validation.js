export const MIGRATION_DIR_PATTERN = /^\d{10}_[a-z0-9-]+$/;
export const validateMigrationDirs = (dirNames, existingSqlFiles) => {
    const errors = [];
    for (const dirName of dirNames) {
        if (!MIGRATION_DIR_PATTERN.test(dirName)) {
            errors.push({ type: 'invalid_dir_name', dirName });
            continue;
        }
        if (!existingSqlFiles.has(dirName)) {
            errors.push({ type: 'missing_sql_file', dirName });
        }
    }
    if (errors.length > 0) {
        return { valid: false, errors };
    }
    const sorted = [...dirNames].sort();
    return { valid: true, dirs: sorted };
};
export const formatValidationErrors = (errors) => {
    const lines = errors.map((error) => {
        if (error.type === 'invalid_dir_name') {
            return `  - "${error.dirName}" does not match the required pattern "<Unix-timestamp>_<slug>" (e.g. "1700000000_create-users"). Slugs must be lowercase alphanumeric with hyphens.`;
        }
        // eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
        if (error.type === 'missing_sql_file') {
            return `  - "${error.dirName}/migration.sql" is missing.`;
        }
        return `  - "${error.dirName}": unknown validation error.`;
    });
    return `Database migration validation failed:\n${lines.join('\n')}`;
};
