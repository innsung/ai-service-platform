import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuthStore } from "@/store/authStore";

import Layout from "./pages/Layout.jsx";
import Home from "./pages/Home.jsx";
import Products from "./pages/Products.jsx";
import ProductDetail from "./pages/ProductDetail.jsx";
import Cart from "./pages/Cart.jsx";
import Checkout from "./pages/Checkout.jsx";
import PayResult from "./pages/PayResult.jsx";
import Login from "./pages/Login.jsx";
import Signup from "./pages/Signup.jsx";
import Support from "./pages/Support.jsx";

import "@/styles/cgvSignup.css";
import "@/styles/cgv.css";
import "@/styles/commons.css";
import "@/styles/shoppy.css";
import "@/styles/cart.css";
import "@/styles/checkoutinfo.css";

// ✅ 로그인 필요한 페이지 보호
const PrivateRoute = ({ children }) => {
  const isLogin = useAuthStore((s) => s.isLogin);
  return isLogin ? children : <Navigate to="/login" replace />;
};

export default function App() {
  // 로그인 상태는 zustand persist(localStorage)로 이미 복구되어 있으므로
  // 별도의 서버 확인 없이 바로 렌더링합니다.
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="products" element={<Products />} />
          <Route path="products/:pid" element={<ProductDetail />} />
          {/* <Route path="cart" element={<Cart />} /> */}
          <Route
            path="cart"
            element={
              <PrivateRoute>
                <Cart />
              </PrivateRoute>
            }
          />
          <Route
            path="checkout"
            element={
              <PrivateRoute>
                <Checkout />
              </PrivateRoute>
            }
          />
          <Route path="payresult" element={<PayResult />} />
          <Route path="login" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route path="support" element={<Support />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
