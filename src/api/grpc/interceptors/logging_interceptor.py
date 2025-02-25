import grpc
import datetime


class LoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        start_time = datetime.datetime.now(datetime.timezone.utc)
        response = continuation(handler_call_details)
        end_time = datetime.datetime.now(datetime.timezone.utc)

        print(
            f"[gRPC LOG] Method: {handler_call_details.method}, Duration: {end_time - start_time}"
        )
        return response
