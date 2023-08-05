/* Configure Boost.Outcome with Boost
(C) 2015-2020 Niall Douglas <http://www.nedproductions.biz/> (7 commits)
File Created: August 2015


Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
*/

#ifndef BOOST_OUTCOME_V2_CONFIG_HPP
#define BOOST_OUTCOME_V2_CONFIG_HPP

#include "detail/version.hpp"

// Pull in detection of __MINGW64_VERSION_MAJOR
#if defined(__MINGW32__) && !defined(DOXYGEN_IS_IN_THE_HOUSE)
#include <_mingw.h>
#endif

#include <boost/config.hpp>

#ifdef BOOST_NO_CXX11_VARIADIC_TEMPLATES
#error Boost.Outcome needs variadic template support in the compiler
#endif
#if defined(BOOST_NO_CXX14_CONSTEXPR) && _MSC_FULL_VER < 191100000
#error Boost.Outcome needs constexpr (C++ 14) support in the compiler
#endif
#ifdef BOOST_NO_CXX14_VARIABLE_TEMPLATES
#error Boost.Outcome needs variable template support in the compiler
#endif
#if !defined(__clang__) && defined(__GNUC__) && __GNUC__ < 6
#error Due to a bug in nested template variables parsing, Boost.Outcome does not work on GCCs earlier than v6.
#endif

#ifndef BOOST_OUTCOME_SYMBOL_VISIBLE
#define BOOST_OUTCOME_SYMBOL_VISIBLE BOOST_SYMBOL_VISIBLE
#endif
#ifdef __has_cpp_attribute
#define BOOST_OUTCOME_HAS_CPP_ATTRIBUTE(attr) __has_cpp_attribute(attr)
#else
#define BOOST_OUTCOME_HAS_CPP_ATTRIBUTE(attr) (0)
#endif
// Weird that Boost.Config doesn't define a BOOST_NO_CXX17_NODISCARD
#ifndef BOOST_OUTCOME_NODISCARD
#if BOOST_OUTCOME_HAS_CPP_ATTRIBUTE(nodiscard)
#define BOOST_OUTCOME_NODISCARD [[nodiscard]]
#elif defined(__clang__)  // deliberately not GCC
#define BOOST_OUTCOME_NODISCARD __attribute__((warn_unused_result))
#elif defined(_MSC_VER)
// _Must_inspect_result_ expands into this
#define BOOST_OUTCOME_NODISCARD                                                                                                                                                                                                                                                                                                \
  __declspec("SAL_name"                                                                                                                                                                                                                                                                                                        \
             "("                                                                                                                                                                                                                                                                                                               \
             "\"_Must_inspect_result_\""                                                                                                                                                                                                                                                                                       \
             ","                                                                                                                                                                                                                                                                                                               \
             "\"\""                                                                                                                                                                                                                                                                                                            \
             ","                                                                                                                                                                                                                                                                                                               \
             "\"2\""                                                                                                                                                                                                                                                                                                           \
             ")") __declspec("SAL_begin") __declspec("SAL_post") __declspec("SAL_mustInspect") __declspec("SAL_post") __declspec("SAL_checkReturn") __declspec("SAL_end")
#endif
#endif
#ifndef BOOST_OUTCOME_NODISCARD
#define BOOST_OUTCOME_NODISCARD
#endif
#ifndef BOOST_OUTCOME_THREAD_LOCAL
#ifndef BOOST_NO_CXX11_THREAD_LOCAL
#define BOOST_OUTCOME_THREAD_LOCAL thread_local
#else
#if defined(_MSC_VER)
#define BOOST_OUTCOME_THREAD_LOCAL __declspec(thread)
#elif defined(__GNUC__)
#define BOOST_OUTCOME_THREAD_LOCAL __thread
#else
#error Unknown compiler, cannot set BOOST_OUTCOME_THREAD_LOCAL
#endif
#endif
#endif
// Can't use the QuickCppLib preprocessor metaprogrammed Concepts TS support, so ...
#ifndef BOOST_OUTCOME_TEMPLATE
#define BOOST_OUTCOME_TEMPLATE(...) template <__VA_ARGS__
#endif
#ifndef BOOST_OUTCOME_TREQUIRES
#define BOOST_OUTCOME_TREQUIRES(...) , __VA_ARGS__ >
#endif
#ifndef BOOST_OUTCOME_TEXPR
#define BOOST_OUTCOME_TEXPR(...) typename = decltype(__VA_ARGS__)
#endif
#ifndef BOOST_OUTCOME_TPRED
#define BOOST_OUTCOME_TPRED(...) typename = std::enable_if_t<__VA_ARGS__>
#endif
#ifndef BOOST_OUTCOME_REQUIRES
#if defined(__cpp_concepts) && (!defined(_MSC_VER) || _MSC_FULL_VER >= 192400000)  // VS 2019 16.3 is broken here
#define BOOST_OUTCOME_REQUIRES(...) requires(__VA_ARGS__)
#else
#define BOOST_OUTCOME_REQUIRES(...)
#endif
#endif

#ifndef BOOST_OUTCOME_ENABLE_LEGACY_SUPPORT_FOR
#define BOOST_OUTCOME_ENABLE_LEGACY_SUPPORT_FOR 210  // the v2.1 Outcome release
#endif

namespace boost
{
#define BOOST_OUTCOME_V2
  //! The Boost.Outcome namespace
  namespace outcome_v2
  {
  }
}
/*! The namespace of this Boost.Outcome v2.
*/
#define BOOST_OUTCOME_V2_NAMESPACE boost::outcome_v2
/*! Expands into the appropriate namespace markup to enter the Boost.Outcome v2 namespace.
*/
#define BOOST_OUTCOME_V2_NAMESPACE_BEGIN                                                                                                                                                                                                                                                                                       \
  namespace boost                                                                                                                                                                                                                                                                                                              \
  {                                                                                                                                                                                                                                                                                                                            \
    namespace outcome_v2                                                                                                                                                                                                                                                                                                       \
    {
/*! Expands into the appropriate namespace markup to enter the C++ module
exported Boost.Outcome v2 namespace.
*/
#define BOOST_OUTCOME_V2_NAMESPACE_EXPORT_BEGIN                                                                                                                                                                                                                                                                                \
  namespace boost                                                                                                                                                                                                                                                                                                              \
  {                                                                                                                                                                                                                                                                                                                            \
    namespace outcome_v2                                                                                                                                                                                                                                                                                                       \
    {
/*! \brief Expands into the appropriate namespace markup to exit the Boost.Outcome v2 namespace.
\ingroup config
*/
#define BOOST_OUTCOME_V2_NAMESPACE_END                                                                                                                                                                                                                                                                                         \
  }                                                                                                                                                                                                                                                                                                                            \
  }

#include <cstdint>  // for uint32_t etc
#include <initializer_list>
#include <iosfwd>  // for future serialisation
#include <new>     // for placement in moves etc
#include <type_traits>

#ifndef BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE
#if defined(_MSC_VER) && _HAS_CXX17
#define BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE 1  // MSVC always has std::in_place_type
#elif __cplusplus >= 201700
// libstdc++ before GCC 6 doesn't have it, despite claiming C++ 17 support
#ifdef __has_include
#if !__has_include(<variant>)
#define BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE 0  // must have it if <variant> is present
#endif
#endif

#ifndef BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE
#define BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE 1
#endif
#else
#define BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE 0
#endif
#endif

#if BOOST_OUTCOME_USE_STD_IN_PLACE_TYPE
#include <utility>  // for in_place_type_t

BOOST_OUTCOME_V2_NAMESPACE_BEGIN
template <class T> using in_place_type_t = std::in_place_type_t<T>;
using std::in_place_type;
BOOST_OUTCOME_V2_NAMESPACE_END
#else
BOOST_OUTCOME_V2_NAMESPACE_BEGIN
//! Aliases `std::in_place_type_t<T>` if on C++ 17 or later, else defined locally.
template <class T> struct in_place_type_t
{
  explicit in_place_type_t() = default;
};
//! Aliases `std::in_place_type<T>` if on C++ 17 or later, else defined locally.
template <class T> constexpr in_place_type_t<T> in_place_type{};
BOOST_OUTCOME_V2_NAMESPACE_END
#endif

#ifndef BOOST_OUTCOME_TRIVIAL_ABI
#if defined(STANDARDESE_IS_IN_THE_HOUSE) || __clang_major__ >= 7
//! Defined to be `[[clang::trivial_abi]]` when on a new enough clang compiler. Usually automatic, can be overriden.
#define BOOST_OUTCOME_TRIVIAL_ABI [[clang::trivial_abi]]
#else
#define BOOST_OUTCOME_TRIVIAL_ABI
#endif
#endif

BOOST_OUTCOME_V2_NAMESPACE_BEGIN
namespace detail
{
  // Test if type is an in_place_type_t
  template <class T> struct is_in_place_type_t
  {
    static constexpr bool value = false;
  };
  template <class U> struct is_in_place_type_t<in_place_type_t<U>>
  {
    static constexpr bool value = true;
  };

  // Replace void with constructible void_type
  struct empty_type
  {
  };
  struct void_type
  {
    // We always compare true to another instance of me
    constexpr bool operator==(void_type /*unused*/) const noexcept { return true; }
    constexpr bool operator!=(void_type /*unused*/) const noexcept { return false; }
  };
  template <class T> using devoid = std::conditional_t<std::is_void<T>::value, void_type, T>;

  template <class Output, class Input> using rebind_type5 = Output;
  template <class Output, class Input>
  using rebind_type4 = std::conditional_t<                                   //
  std::is_volatile<Input>::value,                                            //
  std::add_volatile_t<rebind_type5<Output, std::remove_volatile_t<Input>>>,  //
  rebind_type5<Output, Input>>;
  template <class Output, class Input>
  using rebind_type3 = std::conditional_t<                             //
  std::is_const<Input>::value,                                         //
  std::add_const_t<rebind_type4<Output, std::remove_const_t<Input>>>,  //
  rebind_type4<Output, Input>>;
  template <class Output, class Input>
  using rebind_type2 = std::conditional_t<                                            //
  std::is_lvalue_reference<Input>::value,                                             //
  std::add_lvalue_reference_t<rebind_type3<Output, std::remove_reference_t<Input>>>,  //
  rebind_type3<Output, Input>>;
  template <class Output, class Input>
  using rebind_type = std::conditional_t<                                             //
  std::is_rvalue_reference<Input>::value,                                             //
  std::add_rvalue_reference_t<rebind_type2<Output, std::remove_reference_t<Input>>>,  //
  rebind_type2<Output, Input>>;

  // static_assert(std::is_same_v<rebind_type<int, volatile const double &&>, volatile const int &&>, "");


  /* True if type is the same or constructible. Works around a bug where clang + libstdc++
  pukes on std::is_constructible<filesystem::path, void> (this bug is fixed upstream).
  */
  template <class T, class U> struct _is_explicitly_constructible
  {
    static constexpr bool value = std::is_constructible<T, U>::value;
  };
  template <class T> struct _is_explicitly_constructible<T, void>
  {
    static constexpr bool value = false;
  };
  template <> struct _is_explicitly_constructible<void, void>
  {
    static constexpr bool value = false;
  };
  template <class T, class U> static constexpr bool is_explicitly_constructible = _is_explicitly_constructible<T, U>::value;

  template <class T, class U> struct _is_implicitly_constructible
  {
    static constexpr bool value = std::is_convertible<U, T>::value;
  };
  template <class T> struct _is_implicitly_constructible<T, void>
  {
    static constexpr bool value = false;
  };
  template <> struct _is_implicitly_constructible<void, void>
  {
    static constexpr bool value = false;
  };
  template <class T, class U> static constexpr bool is_implicitly_constructible = _is_implicitly_constructible<T, U>::value;

  template <class T, class... Args> struct _is_nothrow_constructible
  {
    static constexpr bool value = std::is_nothrow_constructible<T, Args...>::value;
  };
  template <class T> struct _is_nothrow_constructible<T, void>
  {
    static constexpr bool value = false;
  };
  template <> struct _is_nothrow_constructible<void, void>
  {
    static constexpr bool value = false;
  };
  template <class T, class... Args> static constexpr bool is_nothrow_constructible = _is_nothrow_constructible<T, Args...>::value;

  template <class T, class... Args> struct _is_constructible
  {
    static constexpr bool value = std::is_constructible<T, Args...>::value;
  };
  template <class T> struct _is_constructible<T, void>
  {
    static constexpr bool value = false;
  };
  template <> struct _is_constructible<void, void>
  {
    static constexpr bool value = false;
  };
  template <class T, class... Args> static constexpr bool is_constructible = _is_constructible<T, Args...>::value;

#ifndef BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE
#if defined(_MSC_VER) && _HAS_CXX17
#define BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE 1  // MSVC always has std::is_nothrow_swappable
#elif __cplusplus >= 201700
// libstdc++ before GCC 6 doesn't have it, despite claiming C++ 17 support
#ifdef __has_include
#if !__has_include(<variant>)
#define BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE 0  // must have it if <variant> is present
#endif
#endif

#ifndef BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE
#define BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE 1
#endif
#else
#define BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE 0
#endif
#endif

// True if type is nothrow swappable
#if !defined(STANDARDESE_IS_IN_THE_HOUSE) && BOOST_OUTCOME_USE_STD_IS_NOTHROW_SWAPPABLE
  template <class T> using is_nothrow_swappable = std::is_nothrow_swappable<T>;
#else
  template <class T> struct is_nothrow_swappable
  {
    static constexpr bool value = std::is_nothrow_move_constructible<T>::value && std::is_nothrow_move_assignable<T>::value;
  };
#endif
}  // namespace detail
BOOST_OUTCOME_V2_NAMESPACE_END

#ifndef BOOST_OUTCOME_THROW_EXCEPTION
#include <boost/throw_exception.hpp>
#define BOOST_OUTCOME_THROW_EXCEPTION(expr) BOOST_THROW_EXCEPTION(expr)
#endif

#ifndef BOOST_OUTCOME_AUTO_TEST_CASE
#define BOOST_OUTCOME_AUTO_TEST_CASE(a, b) BOOST_AUTO_TEST_CASE(a)
#endif

#endif
