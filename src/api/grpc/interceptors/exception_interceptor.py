import grpc


class ExceptionInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        try:
            return continuation(handler_call_details)
        except Exception as e:
            print(f"[gRPC ERROR] {e}")
            context = grpc.ServicerContext()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("An internal error occurred.")
            return context
