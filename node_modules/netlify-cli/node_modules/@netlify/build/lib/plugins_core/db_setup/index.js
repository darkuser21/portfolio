import { join } from 'node:path';
import { getPackageJson } from '../../utils/package.js';
const NPM_PACKAGE_NAME = '@netlify/db';
const condition = async ({ buildDir, packagePath, featureFlags }) => {
    if (!featureFlags?.netlify_build_db_setup) {
        return false;
    }
    const { packageJson } = await getPackageJson(buildDir);
    if (hasDBPackage(packageJson)) {
        return true;
    }
    if (packagePath) {
        const { packageJson: workspacePackageJson } = await getPackageJson(join(buildDir, packagePath));
        if (hasDBPackage(workspacePackageJson)) {
            return true;
        }
    }
    return false;
};
const coreStep = async ({ api, branch, constants, context }) => {
    const siteId = constants.SITE_ID;
    // @ts-expect-error This is an internal method for now so it isn't typed yet.
    // eslint-disable-next-line @typescript-eslint/no-unsafe-call
    const database = (await api.createSiteDatabase({ site_id: siteId }));
    let connectionString = database.connection_string;
    if (context !== 'production') {
        // @ts-expect-error This is an internal method for now so it isn't typed yet.
        // eslint-disable-next-line @typescript-eslint/no-unsafe-call
        const databaseBranch = (await api.createSiteDatabaseBranch({
            site_id: siteId,
            body: { branch_id: branch },
        }));
        connectionString = databaseBranch.connection_string;
    }
    process.env.NETLIFY_DB_URL = connectionString;
    return { newEnvChanges: { NETLIFY_DB_URL: connectionString } };
};
const hasDBPackage = (packageJSON) => {
    const { dependencies = {}, devDependencies = {} } = packageJSON;
    return NPM_PACKAGE_NAME in dependencies || NPM_PACKAGE_NAME in devDependencies;
};
export const dbSetup = {
    event: 'onPreBuild',
    coreStep,
    coreStepId: 'db_provision',
    coreStepName: 'Netlify DB setup',
    coreStepDescription: () => 'Setup Netlify DB database',
    condition,
};
