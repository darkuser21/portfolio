import { CookieStore } from '../cookie_store.js';
import type { RequestHandler } from '../function.js';
import { NetlifyRequest } from '../request.js';
import type { RequestContext } from '../request.js';
export interface PrepareRequestOptions {
    funcPath: string;
    url: string;
    headers: Headers;
    method: string;
    body?: BodyInit | null;
}
export declare const prepareRequest: ({ funcPath, url, headers, method, body }: PrepareRequestOptions) => Promise<{
    req: NetlifyRequest;
    requestContext: RequestContext;
    state: import("../context.js").State;
    cookies: CookieStore;
    importDurationMs: number;
    funcModule: RequestHandler;
}>;
