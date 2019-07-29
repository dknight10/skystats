import { Injectable } from '@angular/core';
import createAuth0Client from '@auth0/auth0-spa-js';
import Auth0Client from '@auth0/auth0-spa-js/dist/typings/Auth0Client';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isAuthenticated = new BehaviorSubject(false);
  profile = new BehaviorSubject<any>(null);

  private auth0Client: Auth0Client;

  // Auth0 application configuration
  config = {
    domain: "dk-test.auth0.com",
    client_id: "Ds252C21hi10xyNPhkkiC10Vibm3dIAv",
    redirect_uri: `${window.location.origin}/callback`,
    audience: "https://skytrakstats.com/api"
  };

  /**
   * Gets the Auth0Client instance.
   */
  async getAuth0Client(): Promise<Auth0Client> {
    if (!this.auth0Client) {
      this.auth0Client = await createAuth0Client(this.config);

      // Provide the current value of isAuthenticated
      this.isAuthenticated.next(await this.auth0Client.isAuthenticated());

      // Whenever isAuthenticated changes, provide the current value of `getUser`
      this.isAuthenticated.subscribe(async isAuthenticated => {
        if (isAuthenticated) {
          this.profile.next(await this.auth0Client.getUser());

          return;
        }

        this.profile.next(null);
      });
    }

    return this.auth0Client;
  }
}