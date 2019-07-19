import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap, mergeMap } from 'rxjs/operators';

import { environment } from '../../../environments/environment';

import { Session, SessionCreator } from './session';

@Injectable({
  providedIn: 'root'
})
export class SessionsService {

  private sessionsUrl = `${environment['api_endpoint']}/v1/sessions`

  constructor(private http: HttpClient) { }

  getSessions(): Observable<Session[]> {
    return this.http.get<Session[]>(this.sessionsUrl + '/')
      .pipe(
        map(response => response.map(e => SessionCreator.create(e))),
        catchError(this.handleError<Session[]>('getSessions', []))
      );
  }

  download(ids: number[], format: string) {
    let url = `${this.sessionsUrl}?action=download&format=${format}&id=${ids.join()}`
    console.log(url)
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      console.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}

