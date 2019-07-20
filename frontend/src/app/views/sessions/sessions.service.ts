import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap, mergeMap } from 'rxjs/operators';

import { environment } from '../../../environments/environment';

import { Session, SessionCreator } from './session';
import { saveFile, getFileNameFromResponseContentDisposition } from '../../util/file-download-util';

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
    let url = `${this.sessionsUrl}?action=download&type=excel&id=${ids.join()}`
    return this.http.get<any>(url, { responseType: "blob" as "json", observe: 'response' })
      .pipe(
        map(res => {
          const fileName = getFileNameFromResponseContentDisposition(res);
          saveFile(res.body, fileName);
        }),
        catchError(this.handleError<any[]>('download', []))
      );
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

