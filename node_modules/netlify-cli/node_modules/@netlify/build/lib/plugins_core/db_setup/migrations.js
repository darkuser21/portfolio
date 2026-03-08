import { copyFile, mkdir, readdir, stat } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { pathExists } from 'path-exists';
import { validateMigrationDirs, formatValidationErrors } from './validation.js';
const condition = async ({ featureFlags, constants, buildDir }) => {
    if (!featureFlags?.netlify_build_db_setup) {
        return false;
    }
    const srcDir = constants.DB_MIGRATIONS_SRC;
    if (!srcDir) {
        return false;
    }
    return pathExists(resolve(buildDir, srcDir));
};
const coreStep = async ({ constants, buildDir, systemLog }) => {
    const srcDir = resolve(buildDir, constants.DB_MIGRATIONS_SRC);
    const destDir = resolve(buildDir, constants.DB_MIGRATIONS_DIST);
    const entries = await readdir(srcDir);
    const dirNames = [];
    for (const entry of entries) {
        const entryStat = await stat(join(srcDir, entry));
        if (entryStat.isDirectory()) {
            dirNames.push(entry);
        }
    }
    if (dirNames.length === 0) {
        systemLog('No migration directories found, skipping copy.');
        return {};
    }
    const existingSqlFiles = new Set();
    for (const dirName of dirNames) {
        const sqlPath = join(srcDir, dirName, 'migration.sql');
        if (await pathExists(sqlPath)) {
            existingSqlFiles.add(dirName);
        }
    }
    const result = validateMigrationDirs(dirNames, existingSqlFiles);
    if (!result.valid) {
        const message = formatValidationErrors(result.errors);
        throw new Error(message);
    }
    for (const dirName of result.dirs) {
        const migrationDestDir = join(destDir, dirName);
        await mkdir(migrationDestDir, { recursive: true });
        await copyFile(join(srcDir, dirName, 'migration.sql'), join(migrationDestDir, 'migration.sql'));
    }
    systemLog(`Copied ${String(result.dirs.length)} migration(s) to ${destDir}`);
    return {};
};
export const copyDbMigrations = {
    event: 'onBuild',
    coreStep,
    coreStepId: 'db_migrations_copy',
    coreStepName: 'Netlify DB migrations',
    coreStepDescription: () => 'Copy database migrations to internal directory',
    condition,
};
