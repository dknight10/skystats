import { Injectable } from '@angular/core';
import {
    HttpRequest,
    HttpHandler,
    HttpEvent,
    HttpInterceptor
} from '@angular/common/http';
import { AuthService } from '../auth/auth.service';
import { Observable, from } from 'rxjs';
import { switchMap } from 'rxjs/operators';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
    token: any;
    constructor(private authService: AuthService) { }

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        const isAuthenticated$ = from(this.authService.isAuthenticated);
        return isAuthenticated$.pipe(switchMap(isAuthenticated => {
            if (isAuthenticated) {
                const accessToken$ = from(this.authService.getAuth0Client().then(client => client.getTokenSilently()));
                return accessToken$.pipe(switchMap(token => {
                    const headers = request.headers.set('Authorization', 'Bearer ' + token);
                    const authReq = request.clone({ headers });
                    return next.handle(authReq);
                }));
            } else {
                return next.handle(request);
            }
        }))
    };
}